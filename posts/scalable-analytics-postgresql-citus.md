---
title: Building Scalable Real-time Analytics with PostgreSQL Citus
date: December 15, 2024
category: System Design
readTime: 8 min read
excerpt: How we architected a distributed analytics system that processes millions of records in real-time using PostgreSQL Citus extension, handling complex aggregations and maintaining sub-second query performance.
---

![Analytics Dashboard](https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80)

When we started building our real-time analytics dashboard at Accredible, we faced a classic challenge: how do you process millions of database records efficiently while maintaining sub-second query performance? The answer lay in PostgreSQL's Citus extension, which transformed our approach to distributed data processing.

## The Challenge

Our analytics system needed to handle complex aggregations across multiple dimensions:

- Time-based analytics (daily, weekly, monthly rollups)
- Geographic distribution of credential issuance
- Institution-specific performance metrics
- Real-time user engagement tracking

Traditional approaches would have required complex data pipeline architectures, but we found a more elegant solution.

## Why PostgreSQL Citus?

Citus extends PostgreSQL with distributed computing capabilities while maintaining the familiar SQL interface. Here's what made it perfect for our use case:

> "Citus allows you to scale PostgreSQL horizontally across multiple machines, turning a cluster of PostgreSQL instances into a single logical database."

### Key Benefits

- **Horizontal Scaling**: Distribute data across multiple nodes
- **SQL Compatibility**: No need to learn new query languages
- **Real-time Ingestion**: Handle high-throughput writes
- **Parallel Processing**: Queries execute across all nodes simultaneously

## Architecture Overview

Our distributed analytics architecture consists of three main components:

### 1. Data Ingestion Layer

```ruby
class AnalyticsEventProcessor
  def process_credential_issued(credential)
    AnalyticsEvent.create!(
      event_type: 'credential_issued',
      institution_id: credential.institution_id,
      issued_at: credential.created_at,
      metadata: {
        credential_type: credential.template.name,
        recipient_location: credential.recipient.location,
        issuer_id: credential.issuer_id
      }
    )
  end

  def process_batch(events)
    AnalyticsEvent.insert_all(events.map(&:to_hash))
  end
end
```

### 2. Distributed Storage with Citus

We partition our data by institution_id to ensure related analytics queries hit the same shard:

```sql
-- Create distributed table
CREATE TABLE analytics_events (
    id BIGSERIAL,
    event_type VARCHAR(50) NOT NULL,
    institution_id BIGINT NOT NULL,
    issued_at TIMESTAMP NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Distribute the table
SELECT create_distributed_table('analytics_events', 'institution_id');

-- Create time-based index for efficient queries
CREATE INDEX idx_analytics_events_time 
ON analytics_events (institution_id, issued_at DESC);
```

### 3. Rollup Tables for Performance

To handle complex aggregations efficiently, we maintain pre-computed rollup tables:

```sql
-- Daily rollups
CREATE TABLE daily_analytics_rollups (
    institution_id BIGINT,
    date DATE,
    credentials_issued INTEGER,
    unique_recipients INTEGER,
    avg_processing_time INTERVAL,
    top_credential_types JSONB
);

-- Distributed rollup table
SELECT create_distributed_table('daily_analytics_rollups', 'institution_id');
```

## Real-world Performance Results

After implementing this architecture, we achieved remarkable performance improvements:

- **Query Performance**: Average query time reduced from 45 seconds to 0.8 seconds
- **Throughput**: Can now handle 50,000+ events per second
- **Scalability**: Linear scaling as we add more worker nodes
- **Reliability**: Built-in replication and failover capabilities

## Lessons Learned

1. **Choose Your Distribution Key Wisely** - The distribution key determines how your data is partitioned. We chose `institution_id` because most queries filter by institution.

2. **Embrace Pre-aggregation** - Rollup tables are essential for complex analytics. Pre-computing during off-peak hours improves dashboard responsiveness.

3. **Monitor Shard Balance** - Regularly check shard distribution to ensure balanced load across worker nodes.

## Conclusion

PostgreSQL Citus enabled us to build a robust, scalable analytics platform without the complexity of traditional big data solutions. By leveraging familiar SQL interfaces and PostgreSQL's reliability, we created a system that scales with our business while maintaining developer productivity.

> "Sometimes the best solutions are the ones that extend what you already know rather than forcing you to learn entirely new paradigms."