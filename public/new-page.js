// New page creation JavaScript
class NewPageCreator {
    constructor() {
        this.form = document.getElementById('newPageForm');
        this.pageNameInput = document.getElementById('pageName');
        this.pageContentInput = document.getElementById('pageContent');
        this.messageDiv = document.getElementById('message');
        this.searchInput = document.getElementById('searchInput');
        this.searchResults = document.getElementById('searchResults');
        
        this.initializeEventListeners();
        this.populateFromURL();
    }

    initializeEventListeners() {
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        
        // Real-time page name validation
        this.pageNameInput.addEventListener('input', (e) => {
            this.validatePageName(e.target.value);
        });

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
                this.handleSubmit(e);
            }
        });
    }

    populateFromURL() {
        // Check if we're creating a specific page from URL
        const urlParams = new URLSearchParams(window.location.search);
        const pageName = urlParams.get('name');
        
        if (pageName) {
            this.pageNameInput.value = pageName;
            this.validatePageName(pageName);
            this.pageContentInput.focus();
        } else {
            this.pageNameInput.focus();
        }
    }

    validatePageName(name) {
        const sanitized = this.sanitizePageName(name);
        
        if (name !== sanitized) {
            this.pageNameInput.value = sanitized;
        }
        
        if (sanitized.length === 0) {
            this.showValidationMessage('Page name cannot be empty', 'error');
        } else if (sanitized.length < 2) {
            this.showValidationMessage('Page name must be at least 2 characters long', 'error');
        } else {
            this.hideMessage();
        }
    }

    async handleSubmit(e) {
        e.preventDefault();
        
        const pageName = this.pageNameInput.value.trim();
        const pageContent = this.pageContentInput.value.trim();
        
        if (!this.validateForm(pageName, pageContent)) {
            return;
        }

        const sanitizedName = this.sanitizePageName(pageName);
        
        try {
            // Check if page already exists
            const checkResponse = await fetch(`/api/page/${sanitizedName}`);
            const existingPage = await checkResponse.json();
            
            if (existingPage.exists) {
                this.showMessage(`Page "${this.formatPageTitle(sanitizedName)}" already exists. Redirecting to edit...`, 'error');
                setTimeout(() => {
                    window.location.href = `/page/${sanitizedName}`;
                }, 2000);
                return;
            }
            
            // Create the page
            const response = await fetch(`/api/page/${sanitizedName}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ content: pageContent })
            });

            const result = await response.json();
            
            if (response.ok) {
                this.showMessage('Page created successfully! Redirecting...', 'success');
                setTimeout(() => {
                    window.location.href = `/page/${sanitizedName}`;
                }, 1000);
            } else {
                this.showMessage(result.error || 'Failed to create page', 'error');
            }
        } catch (error) {
            console.error('Error creating page:', error);
            this.showMessage('Failed to create page', 'error');
        }
    }

    validateForm(pageName, pageContent) {
        if (!pageName) {
            this.showMessage('Page name is required', 'error');
            this.pageNameInput.focus();
            return false;
        }
        
        if (pageName.length < 2) {
            this.showMessage('Page name must be at least 2 characters long', 'error');
            this.pageNameInput.focus();
            return false;
        }
        
        if (!pageContent) {
            this.showMessage('Page content is required', 'error');
            this.pageContentInput.focus();
            return false;
        }
        
        return true;
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
                    <p>Perfect! This would be a great name for a new page.</p>
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

    showValidationMessage(message, type) {
        this.showMessage(message, type);
    }

    hideMessage() {
        this.messageDiv.style.display = 'none';
    }

    sanitizePageName(name) {
        return name.replace(/[^a-zA-Z0-9\-_]/g, '').toLowerCase();
    }

    formatPageTitle(pageName) {
        return pageName.replace(/[-_]/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize the new page creator when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new NewPageCreator();
});