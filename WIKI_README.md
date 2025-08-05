# Simple Wiki 📚

A lightweight, file-based personal wiki application built with Node.js and Express. Create, edit, search, and organize your knowledge with a clean, modern interface.

## Features

- **📝 Markdown Support**: Write content using familiar Markdown syntax
- **🔍 Full-Text Search**: Find any page or content instantly
- **✏️ Live Editing**: Edit pages with real-time preview
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **🔒 Secure**: File-based storage with input sanitization
- **⚡ Fast**: Lightweight and efficient with minimal dependencies
- **🎨 Modern UI**: Beautiful, intuitive interface with smooth animations

## Quick Start

### Prerequisites

- Node.js (version 14 or higher)
- npm (comes with Node.js)

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the server:
   ```bash
   npm start
   ```
4. Open your browser and navigate to `http://localhost:3000`

## Usage

### Creating Pages

1. Click the "New Page" button in the header
2. Enter a descriptive page name (only letters, numbers, hyphens, and underscores)
3. Write your content using Markdown syntax
4. Click "Create Page" to save

### Editing Pages

1. Navigate to any existing page
2. Click the "Edit" button
3. Modify the content in the editor
4. Click "Save Page" or use Ctrl+S

### Searching

- Use the search box in the header to find pages by name or content
- Search results appear in real-time as you type
- Click any result to navigate to that page

### Deleting Pages

1. Navigate to the page you want to delete
2. Click the "Delete" button
3. Confirm the deletion in the dialog

## File Structure

```
simple-wiki/
├── server.js              # Main server application
├── package.json           # Project configuration and dependencies
├── public/                # Static frontend files
│   ├── index.html         # Homepage template
│   ├── page.html          # Page view template
│   ├── new-page.html      # New page creation template
│   ├── style.css          # Application styles
│   ├── app.js             # Homepage JavaScript
│   ├── page.js            # Page view JavaScript
│   └── new-page.js        # New page JavaScript
├── pages/                 # Wiki page storage (created automatically)
│   ├── welcome.md         # Welcome page
│   ├── markdown-guide.md  # Markdown syntax guide
│   └── best-practices.md  # Wiki organization guide
└── README.md              # This file
```

## Configuration

### Environment Variables

- `PORT`: Server port (default: 3000)

### Customization

You can customize the wiki by editing:

- `public/style.css`: Modify the appearance and styling
- `server.js`: Adjust server behavior and API endpoints
- Templates in `public/`: Modify the HTML structure

## API Endpoints

The wiki provides a RESTful API:

- `GET /` - Homepage
- `GET /page/:name` - View page
- `GET /api/pages` - List all pages
- `GET /api/page/:name` - Get page content
- `POST /api/page/:name` - Create or update page
- `DELETE /api/page/:name` - Delete page
- `GET /api/search?q=query` - Search pages

## Security Features

- **Input Sanitization**: All HTML content is sanitized to prevent XSS
- **Rate Limiting**: Prevents abuse with request rate limiting
- **File System Safety**: Page names are sanitized to prevent directory traversal
- **Content Validation**: Server-side validation of all inputs

## Development

### Running in Development Mode

```bash
npm run dev
```

This uses nodemon for automatic server restarts when files change.

### Adding Features

The codebase is modular and easy to extend:

1. **Backend**: Modify `server.js` to add new API endpoints
2. **Frontend**: Add new functionality to the JavaScript files in `public/`
3. **Styling**: Enhance the appearance by editing `public/style.css`

## Backup and Data

### Data Location

All wiki pages are stored as Markdown files in the `pages/` directory. To backup your wiki:

1. Copy the entire `pages/` directory
2. Or set up automated backups of this folder

### Data Migration

To migrate your wiki:

1. Copy the `pages/` directory to your new installation
2. Start the server - all pages will be available immediately

## Troubleshooting

### Common Issues

**Port already in use**
```bash
Error: listen EADDRINUSE :::3000
```
Solution: Either stop the process using port 3000 or set a different port:
```bash
PORT=3001 npm start
```

**Pages directory not found**
The server automatically creates the `pages/` directory on startup.

**Search not working**
Ensure all page files have `.md` extension and are in the `pages/` directory.

### Getting Help

1. Check the [Welcome Page](/page/welcome) for basic usage
2. Review the [Markdown Guide](/page/markdown-guide) for formatting help
3. See [Best Practices](/page/best-practices) for organization tips

## Contributing

This is a simple, self-contained wiki application. Feel free to:

1. Fork the repository
2. Make your improvements
3. Submit a pull request

### Ideas for Enhancements

- **Categories/Tags**: Add page categorization
- **Themes**: Multiple color schemes
- **Export**: Export pages to PDF or other formats
- **Images**: Upload and manage images
- **Users**: Multi-user support with authentication
- **Versions**: Page history and version control

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Technical Details

- **Backend**: Node.js with Express framework
- **Frontend**: Vanilla JavaScript (no frameworks)
- **Storage**: File-based (Markdown files)
- **Markdown Processing**: marked.js library
- **Security**: sanitize-html for XSS prevention
- **Rate Limiting**: express-rate-limit

---

**Start building your knowledge base today!** 🚀

For questions or support, check the example pages included with the wiki or refer to the troubleshooting section above.