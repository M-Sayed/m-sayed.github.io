#!/usr/bin/env python3
"""
Blog Generator - Converts Markdown posts to HTML
Usage: python3 generate-blog.py
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path
import html

# Simple Markdown to HTML converter
class SimpleMarkdown:
    def __init__(self):
        self.code_block_placeholder = "CODE_BLOCK_{}"
        self.code_blocks = {}
        
    def convert(self, text):
        # Store code blocks to prevent processing
        text = self._store_code_blocks(text)
        
        # Convert headers
        text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
        text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
        text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
        
        # Convert bold and italic
        text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        
        # Convert links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        
        # Convert images
        text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
        
        # Convert inline code
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        
        # Convert lists
        text = self._convert_lists(text)
        
        # Convert blockquotes
        text = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)
        
        # Convert paragraphs
        text = self._convert_paragraphs(text)
        
        # Restore code blocks
        text = self._restore_code_blocks(text)
        
        return text
    
    def _store_code_blocks(self, text):
        def replace_code_block(match):
            index = len(self.code_blocks)
            placeholder = self.code_block_placeholder.format(index)
            lang = match.group(1) or ''
            code = html.escape(match.group(2))
            self.code_blocks[placeholder] = f'<pre><code class="language-{lang}">{code}</code></pre>'
            return placeholder
        
        # Match code blocks with optional language
        pattern = r'```(\w*)\n(.*?)```'
        return re.sub(pattern, replace_code_block, text, flags=re.DOTALL)
    
    def _restore_code_blocks(self, text):
        for placeholder, code_html in self.code_blocks.items():
            text = text.replace(placeholder, code_html)
        return text
    
    def _convert_lists(self, text):
        # Convert unordered lists
        lines = text.split('\n')
        in_list = False
        result = []
        
        for line in lines:
            if re.match(r'^- (.+)$', line):
                if not in_list:
                    result.append('<ul>')
                    in_list = True
                result.append(re.sub(r'^- (.+)$', r'<li>\1</li>', line))
            elif in_list and line.strip() == '':
                result.append('</ul>')
                result.append(line)
                in_list = False
            else:
                if in_list:
                    result.append('</ul>')
                    in_list = False
                result.append(line)
        
        if in_list:
            result.append('</ul>')
        
        return '\n'.join(result)
    
    def _convert_paragraphs(self, text):
        # Split into blocks
        blocks = re.split(r'\n\s*\n', text)
        result = []
        
        for block in blocks:
            block = block.strip()
            if block and not re.match(r'^<[^>]+>', block):
                # It's a paragraph
                result.append(f'<p>{block}</p>')
            else:
                result.append(block)
        
        return '\n\n'.join(result)


def parse_frontmatter(content):
    """Parse YAML-like frontmatter from markdown content"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = {}
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
            return frontmatter, parts[2].strip()
    return {}, content


def generate_blog_post_html(metadata, content, template):
    """Generate HTML for a single blog post"""
    md = SimpleMarkdown()
    html_content = md.convert(content)
    
    # Replace placeholders in template
    html = template
    html = html.replace('{{title}}', metadata.get('title', 'Untitled'))
    html = html.replace('{{date}}', metadata.get('date', ''))
    html = html.replace('{{category}}', metadata.get('category', 'General'))
    html = html.replace('{{readTime}}', metadata.get('readTime', '5 min read'))
    html = html.replace('{{content}}', html_content)
    
    return html


def generate_blog_card(metadata, filename):
    """Generate HTML for blog listing card"""
    gradient_map = {
        'System Design': 'var(--gradient-1)',
        'Performance': 'var(--gradient-2)',
        'DevOps': 'var(--gradient-3)',
        'AWS': 'var(--gradient-3)',
        'Ruby on Rails': 'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)',
        'Algorithms': 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
    }
    
    gradient = gradient_map.get(metadata.get('category', ''), 'var(--gradient-1)')
    
    return f'''
            <article class="blog-card">
                <div class="blog-card-image" style="background: {gradient};">
                    {metadata.get('category', 'General')}
                </div>
                <div class="blog-card-content">
                    <h3>{metadata.get('title', 'Untitled')}</h3>
                    <div class="blog-meta">
                        <span>{metadata.get('date', '')}</span>
                        <span>{metadata.get('readTime', '5 min read')}</span>
                        <span>{metadata.get('category', 'General')}</span>
                    </div>
                    <p>{metadata.get('excerpt', '')}</p>
                    <a href="{filename}" class="read-more">
                        Read More →
                    </a>
                </div>
            </article>'''


def load_template():
    """Load the blog post template"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{title}} - Technical blog by Mahmoud Sayed">
    <title>{{title}} - Mahmoud Sayed</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">
                <a href="index.html">
                    <img src="assets/images/logo-v4.svg" alt="Mahmoud Sayed Logo" width="40" height="40">
                </a>
            </div>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Home</a></li>
                <li><a href="index.html#about" class="nav-link">About</a></li>
                <li><a href="index.html#experience" class="nav-link">Experience</a></li>
                <li><a href="index.html#skills" class="nav-link">Skills</a></li>
                <li><a href="index.html#projects" class="nav-link">Projects</a></li>
                <li><a href="index.html#contact" class="nav-link">Contact</a></li>
                <li><a href="blog.html" class="nav-link">Blog</a></li>
            </ul>
            <div class="hamburger">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>

    <article class="blog-post">
        <a href="blog.html" class="back-to-blog">← Back to Blog</a>
        
        <header class="blog-post-header">
            <h1 class="blog-post-title">{{title}}</h1>
            <div class="blog-post-meta">
                Published on {{date}} • {{readTime}} • {{category}}
            </div>
        </header>

        <div class="blog-post-content">
            {{content}}
        </div>
    </article>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 Mahmoud Sayed. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/ruby.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/sql.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
    <script>hljs.highlightAll();</script>
    <script src="assets/js/script.js"></script>
</body>
</html>'''


def update_blog_listing(blog_posts):
    """Update the blog.html file with all blog posts"""
    cards_html = '\n'.join([generate_blog_card(post['metadata'], post['filename']) 
                           for post in blog_posts])
    
    blog_listing_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Technical blog by Mahmoud Sayed - Insights on software engineering, system architecture, and performance optimization">
    <title>Blog - Mahmoud Sayed</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">
                <a href="index.html">
                    <img src="assets/images/logo-v4.svg" alt="Mahmoud Sayed Logo" width="40" height="40">
                </a>
            </div>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">Home</a></li>
                <li><a href="index.html#about" class="nav-link">About</a></li>
                <li><a href="index.html#experience" class="nav-link">Experience</a></li>
                <li><a href="index.html#skills" class="nav-link">Skills</a></li>
                <li><a href="index.html#projects" class="nav-link">Projects</a></li>
                <li><a href="index.html#contact" class="nav-link">Contact</a></li>
                <li><a href="blog.html" class="nav-link active">Blog</a></li>
            </ul>
            <div class="hamburger">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>

    <div class="blog-container">
        <div class="blog-header">
            <h1>Technical Blog</h1>
            <p>Insights on software engineering, system architecture, and performance optimization</p>
        </div>

        <div class="blog-grid">
''' + cards_html + '''
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 Mahmoud Sayed. All rights reserved.</p>
        </div>
    </footer>

    <script src="assets/js/script.js"></script>
</body>
</html>'''
    
    with open('blog.html', 'w') as f:
        f.write(blog_listing_template)


def main():
    posts_dir = Path('posts')
    template = load_template()
    blog_posts = []
    
    # Process all markdown files
    for md_file in posts_dir.glob('*.md'):
        with open(md_file, 'r') as f:
            content = f.read()
        
        metadata, post_content = parse_frontmatter(content)
        
        # Generate output filename
        output_filename = md_file.stem + '.html'
        
        # Generate HTML
        html = generate_blog_post_html(metadata, post_content, template)
        
        # Write HTML file
        with open(output_filename, 'w') as f:
            f.write(html)
        
        # Add to blog posts list
        blog_posts.append({
            'metadata': metadata,
            'filename': output_filename
        })
        
        print(f"✅ Generated: {output_filename}")
    
    # Sort posts by date (newest first)
    blog_posts.sort(key=lambda x: x['metadata'].get('date', ''), reverse=True)
    
    # Update blog listing
    update_blog_listing(blog_posts)
    print(f"\n📝 Updated blog.html with {len(blog_posts)} posts")
    print("\n🎉 Blog generation complete!")


if __name__ == "__main__":
    main()