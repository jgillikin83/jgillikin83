const express = require('express');
const fs = require('fs-extra');
const path = require('path');
const { marked } = require('marked');
const sanitizeHtml = require('sanitize-html');
const rateLimit = require('express-rate-limit');

const app = express();
const PORT = process.env.PORT || 3000;
const PAGES_DIR = path.join(__dirname, 'pages');

// Ensure pages directory exists
fs.ensureDirSync(PAGES_DIR);

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});

app.use(limiter);
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Sanitize HTML configuration
const sanitizeOptions = {
  allowedTags: sanitizeHtml.defaults.allowedTags.concat(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']),
  allowedAttributes: {
    ...sanitizeHtml.defaults.allowedAttributes,
    '*': ['class', 'id']
  }
};

// Helper functions
function getPagePath(pageName) {
  return path.join(PAGES_DIR, `${pageName}.md`);
}

function sanitizePageName(name) {
  return name.replace(/[^a-zA-Z0-9\-_]/g, '').toLowerCase();
}

async function getAllPages() {
  try {
    const files = await fs.readdir(PAGES_DIR);
    return files
      .filter(file => file.endsWith('.md'))
      .map(file => file.replace('.md', ''));
  } catch (error) {
    return [];
  }
}

// Routes
app.get('/', async (req, res) => {
  const pages = await getAllPages();
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/api/pages', async (req, res) => {
  const pages = await getAllPages();
  res.json(pages);
});

app.get('/page/:name', async (req, res) => {
  const pageName = sanitizePageName(req.params.name);
  const pagePath = getPagePath(pageName);
  
  try {
    if (await fs.pathExists(pagePath)) {
      res.sendFile(path.join(__dirname, 'public', 'page.html'));
    } else {
      res.sendFile(path.join(__dirname, 'public', 'new-page.html'));
    }
  } catch (error) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/api/page/:name', async (req, res) => {
  const pageName = sanitizePageName(req.params.name);
  const pagePath = getPagePath(pageName);
  
  try {
    if (await fs.pathExists(pagePath)) {
      const content = await fs.readFile(pagePath, 'utf8');
      const htmlContent = marked(content);
      const sanitizedContent = sanitizeHtml(htmlContent, sanitizeOptions);
      
      res.json({
        name: pageName,
        content: content,
        html: sanitizedContent,
        exists: true
      });
    } else {
      res.json({
        name: pageName,
        content: '',
        html: '',
        exists: false
      });
    }
  } catch (error) {
    res.status(500).json({ error: 'Failed to read page' });
  }
});

app.post('/api/page/:name', async (req, res) => {
  const pageName = sanitizePageName(req.params.name);
  const { content } = req.body;
  
  if (!content || typeof content !== 'string') {
    return res.status(400).json({ error: 'Content is required' });
  }
  
  const pagePath = getPagePath(pageName);
  
  try {
    await fs.writeFile(pagePath, content, 'utf8');
    const htmlContent = marked(content);
    const sanitizedContent = sanitizeHtml(htmlContent, sanitizeOptions);
    
    res.json({
      name: pageName,
      content: content,
      html: sanitizedContent,
      message: 'Page saved successfully'
    });
  } catch (error) {
    res.status(500).json({ error: 'Failed to save page' });
  }
});

app.delete('/api/page/:name', async (req, res) => {
  const pageName = sanitizePageName(req.params.name);
  const pagePath = getPagePath(pageName);
  
  try {
    if (await fs.pathExists(pagePath)) {
      await fs.unlink(pagePath);
      res.json({ message: 'Page deleted successfully' });
    } else {
      res.status(404).json({ error: 'Page not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete page' });
  }
});

app.get('/api/search', async (req, res) => {
  const { q } = req.query;
  
  if (!q || typeof q !== 'string') {
    return res.json([]);
  }
  
  const searchTerm = q.toLowerCase();
  const pages = await getAllPages();
  const results = [];
  
  for (const pageName of pages) {
    try {
      const content = await fs.readFile(getPagePath(pageName), 'utf8');
      if (pageName.toLowerCase().includes(searchTerm) || 
          content.toLowerCase().includes(searchTerm)) {
        results.push({
          name: pageName,
          title: pageName.replace(/[-_]/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
          snippet: content.substring(0, 200) + (content.length > 200 ? '...' : '')
        });
      }
    } catch (error) {
      // Skip this page if there's an error reading it
    }
  }
  
  res.json(results);
});

app.listen(PORT, () => {
  console.log(`Wiki server running on http://localhost:${PORT}`);
});