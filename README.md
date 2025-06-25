# Mahmoud Sayed - Personal Website

A modern, responsive personal website showcasing my software engineering experience, skills, and technical blog. Built with pure HTML, CSS, and JavaScript - no framework dependencies!

## 🌟 Features

- **Responsive Design** - Optimized for all devices
- **Modern UI/UX** - Clean, professional design with smooth animations
- **Technical Blog** - Full-featured blog with syntax highlighting
- **Performance Optimized** - Fast loading and smooth interactions
- **SEO Friendly** - Optimized for search engines
- **No Build Process** - Pure static site, works everywhere

## 🚀 Live Demo

Visit the live website: [https://m-sayed.github.io](https://m-sayed.github.io)

## 🏃‍♂️ Run Locally

### Method 1: Ruby Server (Recommended)
```bash
# Run the Ruby server
ruby server.rb

# Or make it executable and run directly
chmod +x server.rb
./server.rb
```

### Method 2: Python Simple Server
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

### Method 3: Direct File Access
Simply open `index.html` in your web browser!

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: CSS Grid, Flexbox, CSS Variables
- **Syntax Highlighting**: Highlight.js
- **Fonts**: Inter (Google Fonts)
- **Deployment**: GitHub Pages
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
├── index.html              # Main homepage
├── blog.html              # Blog listing page
├── assets/                # Static assets
│   ├── css/
│   │   └── styles.css    # Main stylesheet
│   └── js/
│       └── script.js     # JavaScript functionality
├── posts/                 # Markdown blog posts
│   ├── new-blog-template.md
│   └── *.md              # Your blog posts
├── generate-blog.py       # Blog generator script
├── server.rb             # Ruby development server
├── .nojekyll             # GitHub Pages config
├── CNAME                 # Custom domain (optional)
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions deployment
└── README.md             # This file
```

## 🚀 Deployment to GitHub Pages

### Option 1: GitHub Pages with Actions (Recommended)
1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/[username]/[username].github.io.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**:
   - Go to Settings → Pages
   - Source: GitHub Actions (the workflow will auto-deploy)

### Option 2: Direct GitHub Pages
1. **Push to GitHub** (same as above)
2. **Enable GitHub Pages**:
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / folder: / (root)

### Option 3: Manual Upload
1. **Create repository** named `[username].github.io`
2. **Upload all files** via GitHub web interface
3. **Enable Pages** in settings

The site will be live at `https://[username].github.io` in 5-10 minutes!

### Custom Domain (Optional)

1. **Purchase a domain** from any registrar
2. **Update CNAME file** with your domain:
   ```
   yourdomain.com
   ```
3. **Configure DNS** at your registrar:
   - Add CNAME record pointing to `[your-username].github.io`
4. **Enable custom domain** in GitHub Pages settings

## 🔧 Customization

### Personal Information

Update the following files with your information:

1. **index.html** - Update hero section, experience, skills, projects
2. **styles.css** - Customize colors, fonts, or layout

## ✍️ Blog System

### Easy Blog Creation with Markdown

No more writing HTML! Create blog posts using simple Markdown files:

1. **Create a new Markdown file** in the `posts/` directory:
   ```bash
   cp posts/new-blog-template.md posts/my-new-post.md
   ```

2. **Edit the frontmatter** (metadata at the top):
   ```markdown
   ---
   title: Your Awesome Blog Post
   date: December 25, 2024
   category: Technology
   readTime: 5 min read
   excerpt: A brief description of your post
   ---
   ```

3. **Write your content** using Markdown:
   - Headers: `# H1`, `## H2`, `### H3`
   - Bold: `**text**`
   - Italic: `*text*`
   - Links: `[text](url)`
   - Images: `![alt text](url)`
   - Code blocks: ``` language

4. **Generate HTML**:
   ```bash
   python3 generate-blog.py
   ```

That's it! The script will:
- Convert your Markdown to HTML
- Generate individual blog post pages
- Update the blog listing automatically
- Apply syntax highlighting to code blocks

### Supported Markdown Features

- Headers (H1, H2, H3)
- Bold and italic text
- Links and images
- Code blocks with syntax highlighting
- Blockquotes
- Unordered lists
- Inline code

### Blog Post Template

See `posts/new-blog-template.md` for a complete example with all supported features.

### Color Customization

Modify CSS variables in `styles.css`:

```css
:root {
    --primary-color: #2563eb;    /* Main brand color */
    --secondary-color: #1e40af;  /* Secondary brand color */
    --text-primary: #1f2937;     /* Main text color */
    --text-secondary: #6b7280;   /* Secondary text color */
}
```

## 📊 Performance Features

- **Lazy loading** for images
- **Optimized animations** with CSS transforms
- **Efficient JavaScript** with event delegation
- **Compressed assets** for faster loading
- **Mobile-first** responsive design

## 🔍 SEO Optimization

- Semantic HTML structure
- Meta tags for social sharing
- Structured data markup
- Optimized images with alt text
- Fast loading performance

## 🧪 Testing

### Local Development

1. **Open index.html** in your browser
2. **Use live server** extension in VS Code for hot reload
3. **Test responsiveness** using browser dev tools

### Pre-deployment Checklist

- [ ] All links work correctly
- [ ] Images load properly
- [ ] Responsive design works on all devices
- [ ] Blog posts display correctly
- [ ] Syntax highlighting works
- [ ] Contact links are accurate

## 📝 Content Guidelines

### Blog Posts

- Use meaningful headings (H2, H3)
- Include code examples with proper syntax highlighting
- Add relevant images with alt text
- Keep paragraphs concise and readable
- Include back-to-blog navigation

### Images

- Use high-quality images (preferably 1200px+ width)
- Optimize file sizes for web
- Include descriptive alt text
- Use consistent aspect ratios

## 🤝 Contributing

Feel free to fork this repository and customize it for your own use. If you find bugs or have suggestions for improvements, please open an issue.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **LinkedIn**: [mahmoudsayed15](https://linkedin.com/in/mahmoudsayed15)
- **GitHub**: [m-Sayed](https://github.com/m-Sayed)
- **Website**: [https://m-sayed.github.io](https://m-sayed.github.io)

---

**Built with ❤️ by Mahmoud Sayed**