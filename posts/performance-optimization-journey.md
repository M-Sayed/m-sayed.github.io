---
title: From Minutes to Milliseconds - A Performance Optimization Journey
date: November 28, 2024
category: Performance
readTime: 12 min read
excerpt: A deep dive into how we achieved 10x performance improvements through SQL optimization, strategic caching, and database indexing strategies. Real-world examples and benchmarks included.
---

![Performance Monitoring](https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80)

There's nothing quite like the feeling of transforming a painfully slow query from taking minutes to executing in milliseconds. During my time at Iubenda, I embarked on a performance optimization journey that resulted in 10x faster page load times and 4x improvement in response times. Here's the story of how we achieved these dramatic improvements.

## The Starting Point: A Performance Nightmare

When I joined the team, users were experiencing page load times of 30+ seconds for complex help post searches. The application would sometimes timeout, and the database was constantly under heavy load. Something had to be done.

> "Performance is not just about speed—it's about user experience, business value, and system reliability."

### Initial Metrics

- Average page load time: 32 seconds
- Help post search response: 18 seconds
- Database CPU utilization: 85%
- Cache hit ratio: 12%

## Step 1: Profiling and Identifying Bottlenecks

The first rule of optimization: measure everything. I started by implementing comprehensive profiling across the application stack.

### Rails Profiling Setup

```ruby
class ApplicationController < ActionController::Base
  before_action :start_profiling
  after_action :log_performance_metrics

  private

  def start_profiling
    @start_time = Time.current
    @start_memory = get_memory_usage
  end

  def log_performance_metrics
    duration = Time.current - @start_time
    memory_used = get_memory_usage - @start_memory
    
    Rails.logger.info({
      controller: controller_name,
      action: action_name,
      duration: duration,
      memory_delta: memory_used,
      sql_queries: sql_query_count
    }.to_json)
  end
end
```

### Database Query Analysis

The real culprit was in our database queries. The original problematic query was using ILIKE operators without proper indexing:

```sql
-- Original query taking 18+ seconds
SELECT h.*, u.name as author_name, c.name as category_name
FROM help_posts h
LEFT JOIN users u ON h.user_id = u.id
LEFT JOIN categories c ON h.category_id = c.id
WHERE h.content ILIKE '%search_term%'
   OR h.title ILIKE '%search_term%'
ORDER BY h.created_at DESC
LIMIT 20;
```

## Step 2: Database Optimization

### Strategic Indexing

The first major improvement came from intelligent indexing:

```sql
-- Full-text search indexes
CREATE INDEX idx_help_posts_fulltext ON help_posts 
USING gin(to_tsvector('english', title || ' ' || content));

-- Composite indexes for common filter combinations
CREATE INDEX idx_help_posts_category_date ON help_posts 
(category_id, created_at DESC) WHERE status = 'published';

-- Partial index for active posts only
CREATE INDEX idx_help_posts_active ON help_posts (created_at DESC) 
WHERE status = 'published' AND deleted_at IS NULL;
```

### Query Rewriting

The original query was rewritten to leverage PostgreSQL's full-text search:

```sql
-- Optimized query using full-text search
WITH search_results AS (
  SELECT h.*, 
         ts_rank(to_tsvector('english', h.title || ' ' || h.content), 
                 plainto_tsquery('english', $1)) as rank
  FROM help_posts h
  WHERE h.status = 'published' 
    AND to_tsvector('english', h.title || ' ' || h.content) 
        @@ plainto_tsquery('english', $1)
)
SELECT sr.*, u.name as author_name, c.name as category_name
FROM search_results sr
JOIN users u ON sr.user_id = u.id
JOIN categories c ON sr.category_id = c.id
ORDER BY sr.rank DESC, sr.created_at DESC
LIMIT 20;

-- Query execution time: 45ms (down from 18 seconds!)
```

## Step 3: Strategic Caching Implementation

With database queries optimized, the next focus was intelligent caching:

### Fragment Caching with Smart Invalidation

```ruby
class HelpPost < ApplicationRecord
  after_save :expire_related_caches
  after_destroy :expire_related_caches

  def cache_key_with_version
    "#{cache_key}/#{cache_version}"
  end

  private

  def expire_related_caches
    Rails.cache.delete_matched("help_posts/search/*")
    Rails.cache.delete_matched("help_posts/category/#{category_id}/*")
  end
end
```

## Step 4: Application-Level Optimizations

### N+1 Query Elimination

```ruby
# Before: N+1 queries
def show_help_posts
  @help_posts = HelpPost.published.limit(10)
  # This will trigger N queries for users and N queries for categories
end

# After: Proper eager loading
def show_help_posts
  @help_posts = HelpPost.published
                        .includes(:user, :category, :tags)
                        .limit(10)
end
```

## The Results: Dramatic Performance Gains

After implementing all optimizations, the results were remarkable:

### Before vs After Metrics

- Page Load Time: 32s → 3.2s (10x faster)
- Search Response: 18s → 4.5s (4x faster)
- DB CPU Usage: 85% → 35% (59% reduction)
- Cache Hit Ratio: 12% → 87% (7x improvement)

## Key Lessons Learned

1. **Measure First, Optimize Second** - Without proper profiling, you're optimizing blind.

2. **Database Optimization Has the Biggest Impact** - In most web applications, the database is the bottleneck.

3. **Caching is an Art, Not a Science** - Effective caching requires understanding your application's access patterns.

4. **Monitor Everything** - Performance optimization is an ongoing process.

> "The fastest code is the code that never runs. The second fastest is the code that runs efficiently."

## Conclusion

Performance optimization is a journey, not a destination. By following a systematic approach—profiling, database optimization, strategic caching, and continuous monitoring—we transformed a slow, frustrating user experience into a fast, responsive application.

Remember: every millisecond matters to your users. The effort you put into performance optimization directly translates to better user experience and business value.