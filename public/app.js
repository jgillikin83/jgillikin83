// Main app JavaScript for wiki homepage
class WikiApp {
    constructor() {
        this.searchInput = document.getElementById('searchInput');
        this.pageList = document.getElementById('pageList');
        this.searchResults = document.getElementById('searchResults');
        
        this.initializeEventListeners();
        this.loadPages();
    }

    initializeEventListeners() {
        // Search functionality
        let searchTimeout;
        this.searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            const query = e.target.value.trim();
            
            if (query.length === 0) {
                this.hideSearchResults();
                return;
            }
            
            // Debounce search
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
    }

    async loadPages() {
        try {
            const response = await fetch('/api/pages');
            const pages = await response.json();
            
            this.renderPageList(pages);
        } catch (error) {
            console.error('Error loading pages:', error);
            this.pageList.innerHTML = '<div class="error">Failed to load pages</div>';
        }
    }

    renderPageList(pages) {
        if (pages.length === 0) {
            this.pageList.innerHTML = `
                <div class="page-card">
                    <h3>No pages yet</h3>
                    <p>Create your first wiki page to get started!</p>
                    <a href="/page/new-page" class="btn btn-primary">Create First Page</a>
                </div>
            `;
            return;
        }

        const pageCards = pages.map(page => {
            const title = this.formatPageTitle(page);
            return `
                <div class="page-card">
                    <h3><a href="/page/${page}">${title}</a></h3>
                    <p>Click to view and edit this page</p>
                </div>
            `;
        }).join('');

        this.pageList.innerHTML = pageCards;
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

// Initialize the app when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new WikiApp();
});