// Page view and edit JavaScript
class WikiPage {
    constructor() {
        this.pageName = this.getPageNameFromURL();
        this.pageTitle = document.getElementById('pageTitle');
        this.pageContent = document.getElementById('pageContent');
        this.editorContainer = document.getElementById('editorContainer');
        this.pageEditor = document.getElementById('pageEditor');
        this.editBtn = document.getElementById('editBtn');
        this.deleteBtn = document.getElementById('deleteBtn');
        this.saveBtn = document.getElementById('saveBtn');
        this.cancelBtn = document.getElementById('cancelBtn');
        this.messageDiv = document.getElementById('message');
        this.searchInput = document.getElementById('searchInput');
        this.searchResults = document.getElementById('searchResults');
        
        this.isEditing = false;
        this.originalContent = '';
        
        this.initializeEventListeners();
        this.loadPage();
    }

    getPageNameFromURL() {
        const path = window.location.pathname;
        return path.split('/').pop();
    }

    initializeEventListeners() {
        this.editBtn.addEventListener('click', () => this.startEditing());
        this.deleteBtn.addEventListener('click', () => this.deletePage());
        this.saveBtn.addEventListener('click', () => this.savePage());
        this.cancelBtn.addEventListener('click', () => this.cancelEditing());

        // Search functionality
        let searchTimeout;
        this.searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            const query = e.target.value.trim();
            
            if (query.length === 0) {
                this.hideSearchResults();
                return;
            }
            
            searchTimeout = setTimeout(() => {
                this.performSearch(query);
            }, 300);
        });

        // Clear search when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.search-container') && !e.target.closest('.search-results')) {
                this.hideSearchResults();
                this.searchInput.value = '';
            }
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 's') {
                e.preventDefault();
                if (this.isEditing) {
                    this.savePage();
                }
            }
            if (e.key === 'Escape' && this.isEditing) {
                this.cancelEditing();
            }
        });
    }

    async loadPage() {
        try {
            const response = await fetch(`/api/page/${this.pageName}`);
            const pageData = await response.json();
            
            if (pageData.exists) {
                this.displayPage(pageData);
            } else {
                this.showPageNotFound();
            }
        } catch (error) {
            console.error('Error loading page:', error);
            this.showError('Failed to load page');
        }
    }

    displayPage(pageData) {
        this.pageTitle.textContent = this.formatPageTitle(pageData.name);
        this.pageContent.innerHTML = pageData.html;
        this.originalContent = pageData.content;
        
        // Update page title
        document.title = `${this.formatPageTitle(pageData.name)} - Wiki`;
    }

    showPageNotFound() {
        this.pageTitle.textContent = 'Page Not Found';
        this.pageContent.innerHTML = `
            <div class="message error">
                <h2>Page "${this.formatPageTitle(this.pageName)}" does not exist</h2>
                <p>Would you like to create this page?</p>
                <a href="/page/new-page" class="btn btn-primary">Create New Page</a>
            </div>
        `;
        this.editBtn.style.display = 'none';
        this.deleteBtn.style.display = 'none';
    }

    startEditing() {
        this.isEditing = true;
        this.pageEditor.value = this.originalContent;
        this.pageContent.style.display = 'none';
        this.editorContainer.style.display = 'block';
        this.editBtn.style.display = 'none';
        this.deleteBtn.style.display = 'none';
        this.pageEditor.focus();
    }

    cancelEditing() {
        this.isEditing = false;
        this.pageContent.style.display = 'block';
        this.editorContainer.style.display = 'none';
        this.editBtn.style.display = 'inline-block';
        this.deleteBtn.style.display = 'inline-block';
        this.hideMessage();
    }

    async savePage() {
        const content = this.pageEditor.value.trim();
        
        if (!content) {
            this.showMessage('Page content cannot be empty', 'error');
            return;
        }

        try {
            const response = await fetch(`/api/page/${this.pageName}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ content })
            });

            const result = await response.json();
            
            if (response.ok) {
                this.originalContent = content;
                this.pageContent.innerHTML = result.html;
                this.cancelEditing();
                this.showMessage('Page saved successfully!', 'success');
                
                // Auto-hide success message
                setTimeout(() => this.hideMessage(), 3000);
            } else {
                this.showMessage(result.error || 'Failed to save page', 'error');
            }
        } catch (error) {
            console.error('Error saving page:', error);
            this.showMessage('Failed to save page', 'error');
        }
    }

    async deletePage() {
        if (!confirm(`Are you sure you want to delete the page "${this.formatPageTitle(this.pageName)}"? This action cannot be undone.`)) {
            return;
        }

        try {
            const response = await fetch(`/api/page/${this.pageName}`, {
                method: 'DELETE'
            });

            const result = await response.json();
            
            if (response.ok) {
                this.showMessage('Page deleted successfully!', 'success');
                setTimeout(() => {
                    window.location.href = '/';
                }, 1000);
            } else {
                this.showMessage(result.error || 'Failed to delete page', 'error');
            }
        } catch (error) {
            console.error('Error deleting page:', error);
            this.showMessage('Failed to delete page', 'error');
        }
    }

    async performSearch(query) {
        try {
            const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
            const results = await response.json();
            
            this.renderSearchResults(results, query);
        } catch (error) {
            console.error('Search error:', error);
            this.renderSearchResults([], query);
        }
    }

    renderSearchResults(results, query) {
        if (results.length === 0) {
            this.searchResults.innerHTML = `
                <div class="search-result">
                    <h3>No results found for "${query}"</h3>
                    <p>Try a different search term or <a href="/page/${this.sanitizePageName(query)}">create a new page</a> with this name.</p>
                </div>
            `;
        } else {
            const resultHtml = results.map(result => `
                <div class="search-result">
                    <h3><a href="/page/${result.name}">${result.title}</a></h3>
                    <div class="search-snippet">${this.escapeHtml(result.snippet)}</div>
                </div>
            `).join('');
            
            this.searchResults.innerHTML = resultHtml;
        }
        
        this.showSearchResults();
    }

    showSearchResults() {
        this.searchResults.style.display = 'block';
    }

    hideSearchResults() {
        this.searchResults.style.display = 'none';
    }

    showMessage(message, type) {
        this.messageDiv.textContent = message;
        this.messageDiv.className = `message ${type}`;
        this.messageDiv.style.display = 'block';
    }

    hideMessage() {
        this.messageDiv.style.display = 'none';
    }

    showError(message) {
        this.showMessage(message, 'error');
    }

    formatPageTitle(pageName) {
        return pageName.replace(/[-_]/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    }

    sanitizePageName(name) {
        return name.replace(/[^a-zA-Z0-9\-_]/g, '').toLowerCase();
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize the page when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new WikiPage();
});