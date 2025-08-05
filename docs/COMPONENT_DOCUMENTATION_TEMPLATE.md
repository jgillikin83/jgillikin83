# Component Documentation Template

This template provides standardized formats for documenting UI components across different frameworks and libraries.

## General Component Documentation Structure

### Basic Template

```markdown
## Component: ComponentName

**Description**: Brief description of what the component does and its purpose in the UI.

**Type**: Presentation | Container | Layout | Form | Navigation

### Props/Properties

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `prop1` | `string` | Yes | - | Description of prop1 |
| `prop2` | `number` | No | `0` | Description of prop2 |
| `onEvent` | `function` | No | - | Callback function description |

### Events/Callbacks

- `onEvent`: Triggered when [event description]
- `onChange`: Triggered when [change description]

### Slots/Children

- `default`: Main content area
- `header`: Header content (optional)
- `footer`: Footer content (optional)

### Styling

#### CSS Classes
- `.component-name`: Main container
- `.component-name__element`: Specific element within component
- `.component-name--modifier`: Variant modifier

#### CSS Custom Properties
- `--component-primary-color`: Primary color (default: #007bff)
- `--component-spacing`: Internal spacing (default: 1rem)

### Usage Examples

#### Basic Usage
```jsx
<ComponentName prop1="value" />
```

#### Advanced Usage
```jsx
<ComponentName 
  prop1="value"
  prop2={10}
  onEvent={handleEvent}
>
  Content goes here
</ComponentName>
```

### Accessibility

- ARIA roles and labels
- Keyboard navigation support
- Screen reader compatibility
- Focus management

### Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Notes

- Important usage considerations
- Performance implications
- Known limitations
```

---

## Framework-Specific Templates

### React Component

```markdown
## Component: UserCard

**Description**: A responsive card component that displays user information including avatar, name, role, and contact details with interactive actions.

**Type**: Presentation Component

### Props

```typescript
interface UserCardProps {
  user: {
    id: string;
    name: string;
    email: string;
    avatar?: string;
    role: string;
    department?: string;
    isOnline?: boolean;
  };
  variant?: 'default' | 'compact' | 'detailed';
  showActions?: boolean;
  onEdit?: (userId: string) => void;
  onMessage?: (userId: string) => void;
  onRemove?: (userId: string) => void;
  className?: string;
  style?: React.CSSProperties;
}
```

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `user` | `UserData` | Yes | - | User information object |
| `variant` | `'default' \| 'compact' \| 'detailed'` | No | `'default'` | Visual variant of the card |
| `showActions` | `boolean` | No | `true` | Whether to show action buttons |
| `onEdit` | `(userId: string) => void` | No | - | Callback when edit button is clicked |
| `onMessage` | `(userId: string) => void` | No | - | Callback when message button is clicked |
| `onRemove` | `(userId: string) => void` | No | - | Callback when remove button is clicked |
| `className` | `string` | No | - | Additional CSS classes |
| `style` | `React.CSSProperties` | No | - | Inline styles |

### State

The component manages the following internal state:
- `isExpanded`: boolean for detailed view toggle
- `isLoading`: boolean for async operations
- `imageError`: boolean for avatar loading fallback

### Events

- `onEdit`: Triggered when user clicks the edit button
- `onMessage`: Triggered when user clicks the message button  
- `onRemove`: Triggered when user clicks the remove button (shows confirmation)

### Usage Examples

#### Basic Usage
```jsx
import { UserCard } from './components/UserCard';

const user = {
  id: '123',
  name: 'John Doe',
  email: 'john@example.com',
  role: 'Developer',
  avatar: 'https://example.com/avatar.jpg',
  isOnline: true
};

function App() {
  return <UserCard user={user} />;
}
```

#### With Event Handlers
```jsx
function UserManagement() {
  const handleEdit = (userId) => {
    console.log('Edit user:', userId);
    // Navigate to edit page or open modal
  };

  const handleMessage = (userId) => {
    console.log('Message user:', userId);
    // Open message composer
  };

  const handleRemove = (userId) => {
    console.log('Remove user:', userId);
    // Show confirmation and remove user
  };

  return (
    <UserCard
      user={user}
      variant="detailed"
      onEdit={handleEdit}
      onMessage={handleMessage}
      onRemove={handleRemove}
    />
  );
}
```

#### Different Variants
```jsx
// Compact variant for lists
<UserCard user={user} variant="compact" showActions={false} />

// Detailed variant for profiles
<UserCard user={user} variant="detailed" />

// Custom styling
<UserCard 
  user={user} 
  className="custom-user-card"
  style={{ maxWidth: '300px' }}
/>
```

#### Error Handling
```jsx
function UserCardWithErrorBoundary() {
  return (
    <ErrorBoundary fallback={<div>Error loading user card</div>}>
      <UserCard user={user} />
    </ErrorBoundary>
  );
}
```

### Styling

#### CSS Classes
```css
.user-card {
  /* Main container */
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  background: white;
}

.user-card__avatar {
  /* Avatar container */
  width: 48px;
  height: 48px;
  border-radius: 50%;
}

.user-card__content {
  /* Main content area */
  flex: 1;
  margin-left: 12px;
}

.user-card__name {
  /* User name styling */
  font-weight: 600;
  font-size: 16px;
}

.user-card__role {
  /* Role/title styling */
  color: #666;
  font-size: 14px;
}

.user-card__actions {
  /* Action buttons container */
  display: flex;
  gap: 8px;
  margin-top: 12px;
}

.user-card--compact {
  /* Compact variant modifier */
  padding: 8px;
}

.user-card--detailed {
  /* Detailed variant modifier */
  padding: 24px;
}

.user-card__status-indicator {
  /* Online status indicator */
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #28a745;
}

.user-card__status-indicator--offline {
  background: #6c757d;
}
```

#### CSS Custom Properties
```css
.user-card {
  --user-card-border-color: #e0e0e0;
  --user-card-border-radius: 8px;
  --user-card-padding: 16px;
  --user-card-background: white;
  --user-card-shadow: 0 2px 4px rgba(0,0,0,0.1);
  --user-card-online-color: #28a745;
  --user-card-offline-color: #6c757d;
}
```

### Accessibility

- **ARIA Labels**: Uses `aria-label` for action buttons
- **Keyboard Navigation**: All interactive elements are keyboard accessible
- **Screen Reader Support**: Proper semantic HTML and ARIA attributes
- **Focus Management**: Clear focus indicators and logical tab order
- **Color Contrast**: Meets WCAG AA standards for text contrast

#### Example ARIA Implementation
```jsx
<div 
  className="user-card" 
  role="article" 
  aria-labelledby={`user-name-${user.id}`}
>
  <img 
    src={user.avatar} 
    alt={`${user.name}'s avatar`}
    onError={handleImageError}
  />
  <h3 id={`user-name-${user.id}`}>{user.name}</h3>
  <button 
    onClick={() => onEdit(user.id)}
    aria-label={`Edit ${user.name}'s profile`}
  >
    Edit
  </button>
</div>
```

### Testing

#### Unit Tests
```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import { UserCard } from './UserCard';

const mockUser = {
  id: '123',
  name: 'John Doe',
  email: 'john@example.com',
  role: 'Developer'
};

describe('UserCard', () => {
  test('renders user information', () => {
    render(<UserCard user={mockUser} />);
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('Developer')).toBeInTheDocument();
  });

  test('calls onEdit when edit button is clicked', () => {
    const handleEdit = jest.fn();
    render(<UserCard user={mockUser} onEdit={handleEdit} />);
    
    fireEvent.click(screen.getByLabelText(/edit/i));
    expect(handleEdit).toHaveBeenCalledWith('123');
  });

  test('handles missing avatar gracefully', () => {
    const userWithoutAvatar = { ...mockUser, avatar: undefined };
    render(<UserCard user={userWithoutAvatar} />);
    
    expect(screen.getByText('JD')).toBeInTheDocument(); // Initials fallback
  });
});
```

### Performance Notes

- Uses React.memo for prop change optimization
- Avatar images are lazy-loaded
- Action buttons use event delegation
- Minimal re-renders through proper dependency arrays

### Browser Support

- **Modern Browsers**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Responsive Design**: Works on mobile devices
- **Dark Mode**: Supports system preference detection

### Notes

- Component is fully controlled and doesn't manage user data internally
- Avatar fallback shows user initials when image fails to load
- Remove action shows confirmation dialog before triggering callback
- Supports custom themes through CSS custom properties
- Compatible with React 17+ and React 18
```

### Vue Component

```markdown
## Component: ProductCard

**Description**: A reusable product card component that displays product information with customizable actions and variants for different use cases.

**Type**: Presentation Component

### Props

```typescript
interface ProductCardProps {
  product: {
    id: string;
    name: string;
    price: number;
    currency?: string;
    image?: string;
    description?: string;
    inStock: boolean;
    rating?: number;
    category?: string;
  };
  variant?: 'grid' | 'list' | 'minimal';
  showAddToCart?: boolean;
  showWishlist?: boolean;
  loading?: boolean;
}
```

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `product` | `Product` | Yes | - | Product data object |
| `variant` | `'grid' \| 'list' \| 'minimal'` | No | `'grid'` | Display variant |
| `showAddToCart` | `boolean` | No | `true` | Show add to cart button |
| `showWishlist` | `boolean` | No | `true` | Show wishlist toggle |
| `loading` | `boolean` | No | `false` | Show loading state |

### Events

- `@add-to-cart`: Emitted when add to cart button is clicked
- `@toggle-wishlist`: Emitted when wishlist button is clicked
- `@product-click`: Emitted when product card is clicked

### Slots

- `default`: Replaces entire card content
- `image`: Custom image content
- `title`: Custom title content
- `price`: Custom price display
- `actions`: Custom action buttons

### Usage Examples

#### Basic Usage
```vue
<template>
  <ProductCard 
    :product="product" 
    @add-to-cart="handleAddToCart"
    @toggle-wishlist="handleWishlistToggle"
  />
</template>

<script setup lang="ts">
import { ProductCard } from '@/components/ProductCard.vue';

const product = {
  id: 'prod-123',
  name: 'Wireless Headphones',
  price: 199.99,
  currency: 'USD',
  image: '/images/headphones.jpg',
  description: 'High-quality wireless headphones with noise cancellation',
  inStock: true,
  rating: 4.5,
  category: 'Electronics'
};

const handleAddToCart = (productId: string) => {
  console.log('Add to cart:', productId);
  // Add to cart logic
};

const handleWishlistToggle = (productId: string, inWishlist: boolean) => {
  console.log('Wishlist toggle:', productId, inWishlist);
  // Wishlist logic
};
</script>
```

#### Different Variants
```vue
<template>
  <!-- Grid variant (default) -->
  <ProductCard :product="product" variant="grid" />
  
  <!-- List variant for search results -->
  <ProductCard :product="product" variant="list" />
  
  <!-- Minimal variant for related products -->
  <ProductCard 
    :product="product" 
    variant="minimal"
    :show-add-to-cart="false"
  />
</template>
```

#### With Custom Slots
```vue
<template>
  <ProductCard :product="product">
    <template #image>
      <div class="custom-image-container">
        <img :src="product.image" :alt="product.name" />
        <div class="image-overlay">
          <span class="badge">Sale</span>
        </div>
      </div>
    </template>
    
    <template #price>
      <div class="custom-price">
        <span class="original-price">${{ product.originalPrice }}</span>
        <span class="sale-price">${{ product.price }}</span>
      </div>
    </template>
    
    <template #actions>
      <button @click="buyNow" class="btn-primary">
        Buy Now
      </button>
      <button @click="addToWishlist" class="btn-secondary">
        ♡
      </button>
    </template>
  </ProductCard>
</template>
```

#### Loading State
```vue
<template>
  <ProductCard 
    :product="product"
    :loading="isLoading"
  />
</template>

<script setup>
import { ref } from 'vue';

const isLoading = ref(true);

// Simulate loading
setTimeout(() => {
  isLoading.value = false;
}, 2000);
</script>
```

#### Composition API Usage
```vue
<template>
  <div class="product-grid">
    <ProductCard
      v-for="product in products"
      :key="product.id"
      :product="product"
      @add-to-cart="addToCart"
      @product-click="navigateToProduct"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useCart } from '@/composables/useCart';

const router = useRouter();
const { addItem } = useCart();

const products = ref([]);
const isLoading = ref(false);

const addToCart = async (productId: string) => {
  try {
    await addItem(productId);
    // Show success message
  } catch (error) {
    // Handle error
  }
};

const navigateToProduct = (productId: string) => {
  router.push(`/products/${productId}`);
};
</script>
```

### Styling

#### Component Styles
```vue
<style scoped>
.product-card {
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  padding: var(--card-padding);
  background: var(--card-background);
  transition: all 0.2s ease;
}

.product-card:hover {
  box-shadow: var(--card-shadow-hover);
  transform: translateY(-2px);
}

.product-card--grid {
  display: flex;
  flex-direction: column;
  aspect-ratio: 1;
}

.product-card--list {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.product-card--minimal {
  padding: calc(var(--card-padding) / 2);
}

.product-card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: var(--border-radius);
}

.product-card__content {
  flex: 1;
  padding: 16px 0;
}

.product-card__name {
  font-weight: 600;
  font-size: 16px;
  line-height: 1.4;
  margin-bottom: 8px;
}

.product-card__price {
  font-size: 18px;
  font-weight: 700;
  color: var(--primary-color);
}

.product-card__actions {
  display: flex;
  gap: 8px;
  margin-top: 16px;
}

.product-card__loading {
  opacity: 0.6;
  pointer-events: none;
}

/* Skeleton loading */
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
</style>
```

#### CSS Custom Properties
```css
.product-card {
  --border-color: #e0e0e0;
  --border-radius: 8px;
  --card-padding: 16px;
  --card-background: white;
  --card-shadow-hover: 0 4px 12px rgba(0,0,0,0.15);
  --primary-color: #007bff;
}
```

### Accessibility

- **Semantic HTML**: Uses proper heading hierarchy and button elements
- **ARIA Labels**: Descriptive labels for all interactive elements
- **Keyboard Navigation**: Tab order and Enter/Space key support
- **Screen Reader**: Product information read in logical order
- **Focus Management**: Clear focus indicators

### Testing

#### Component Tests
```javascript
import { mount } from '@vue/test-utils';
import ProductCard from '@/components/ProductCard.vue';

describe('ProductCard', () => {
  const mockProduct = {
    id: 'test-product',
    name: 'Test Product',
    price: 29.99,
    inStock: true
  };

  test('renders product information', () => {
    const wrapper = mount(ProductCard, {
      props: { product: mockProduct }
    });

    expect(wrapper.text()).toContain('Test Product');
    expect(wrapper.text()).toContain('$29.99');
  });

  test('emits add-to-cart event', async () => {
    const wrapper = mount(ProductCard, {
      props: { product: mockProduct }
    });

    await wrapper.find('[data-testid="add-to-cart"]').trigger('click');
    expect(wrapper.emitted('add-to-cart')).toBeTruthy();
    expect(wrapper.emitted('add-to-cart')[0]).toEqual([mockProduct.id]);
  });

  test('shows loading state', () => {
    const wrapper = mount(ProductCard, {
      props: { 
        product: mockProduct, 
        loading: true 
      }
    });

    expect(wrapper.classes()).toContain('product-card__loading');
  });
});
```

### Performance Notes

- Uses `v-memo` for expensive rendering operations
- Image lazy loading with intersection observer
- Computed properties for derived state
- Event handler optimization with proper key usage

### Notes

- Component is reactive to product prop changes
- Supports internationalization through i18n integration
- Image fallback handled automatically
- Compatible with Vue 3.2+ Composition API
- Supports SSR (Server-Side Rendering)
```

### Angular Component

```markdown
## Component: DataTable

**Description**: A feature-rich, accessible data table component with sorting, filtering, pagination, and row selection capabilities.

**Type**: Container Component

### Inputs

```typescript
@Component({
  selector: 'app-data-table',
  templateUrl: './data-table.component.html',
  styleUrls: ['./data-table.component.scss']
})
export class DataTableComponent<T> {
  @Input() data: T[] = [];
  @Input() columns: TableColumn[] = [];
  @Input() loading: boolean = false;
  @Input() selectable: boolean = false;
  @Input() sortable: boolean = true;
  @Input() filterable: boolean = true;
  @Input() paginated: boolean = true;
  @Input() pageSize: number = 10;
  @Input() emptyMessage: string = 'No data available';
  @Input() loadingTemplate?: TemplateRef<any>;
  @Input() rowTemplate?: TemplateRef<any>;
}

interface TableColumn {
  key: string;
  label: string;
  sortable?: boolean;
  filterable?: boolean;
  width?: string;
  align?: 'left' | 'center' | 'right';
  pipe?: string;
  template?: TemplateRef<any>;
}
```

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `data` | `T[]` | Yes | `[]` | Array of data objects to display |
| `columns` | `TableColumn[]` | Yes | `[]` | Column configuration array |
| `loading` | `boolean` | No | `false` | Show loading state |
| `selectable` | `boolean` | No | `false` | Enable row selection |
| `sortable` | `boolean` | No | `true` | Enable column sorting |
| `filterable` | `boolean` | No | `true` | Enable filtering |
| `paginated` | `boolean` | No | `true` | Enable pagination |
| `pageSize` | `number` | No | `10` | Items per page |

### Outputs

```typescript
@Output() rowClick = new EventEmitter<T>();
@Output() rowSelect = new EventEmitter<T[]>();
@Output() sortChange = new EventEmitter<SortEvent>();
@Output() filterChange = new EventEmitter<FilterEvent>();
@Output() pageChange = new EventEmitter<PageEvent>();
```

| Output | Type | Description |
|--------|------|-------------|
| `rowClick` | `EventEmitter<T>` | Emitted when a row is clicked |
| `rowSelect` | `EventEmitter<T[]>` | Emitted when row selection changes |
| `sortChange` | `EventEmitter<SortEvent>` | Emitted when sorting changes |
| `filterChange` | `EventEmitter<FilterEvent>` | Emitted when filters change |
| `pageChange` | `EventEmitter<PageEvent>` | Emitted when page changes |

### Usage Examples

#### Basic Usage
```typescript
// Component
export class UserListComponent {
  users: User[] = [
    { id: 1, name: 'John Doe', email: 'john@example.com', role: 'Admin' },
    { id: 2, name: 'Jane Smith', email: 'jane@example.com', role: 'User' }
  ];

  columns: TableColumn[] = [
    { key: 'id', label: 'ID', width: '80px' },
    { key: 'name', label: 'Name', sortable: true },
    { key: 'email', label: 'Email', sortable: true },
    { key: 'role', label: 'Role', filterable: true }
  ];

  onRowClick(user: User): void {
    console.log('Row clicked:', user);
  }

  onSelectionChange(selectedUsers: User[]): void {
    console.log('Selection changed:', selectedUsers);
  }
}
```

```html
<!-- Template -->
<app-data-table
  [data]="users"
  [columns]="columns"
  [selectable]="true"
  (rowClick)="onRowClick($event)"
  (rowSelect)="onSelectionChange($event)">
</app-data-table>
```

#### Advanced Usage with Custom Templates
```typescript
export class ProductListComponent {
  products: Product[] = [];
  loading = false;

  columns: TableColumn[] = [
    { key: 'image', label: 'Image', width: '100px', template: this.imageTemplate },
    { key: 'name', label: 'Product Name', sortable: true },
    { key: 'price', label: 'Price', sortable: true, pipe: 'currency', align: 'right' },
    { key: 'status', label: 'Status', template: this.statusTemplate },
    { key: 'actions', label: 'Actions', template: this.actionsTemplate, width: '150px' }
  ];

  @ViewChild('imageTemplate', { static: true }) imageTemplate!: TemplateRef<any>;
  @ViewChild('statusTemplate', { static: true }) statusTemplate!: TemplateRef<any>;
  @ViewChild('actionsTemplate', { static: true }) actionsTemplate!: TemplateRef<any>;

  loadProducts(): void {
    this.loading = true;
    this.productService.getProducts().subscribe(products => {
      this.products = products;
      this.loading = false;
    });
  }

  editProduct(product: Product): void {
    // Edit logic
  }

  deleteProduct(product: Product): void {
    // Delete logic
  }
}
```

```html
<app-data-table
  [data]="products"
  [columns]="columns"
  [loading]="loading"
  [pageSize]="25"
  emptyMessage="No products found">

  <!-- Custom image template -->
  <ng-template #imageTemplate let-row="row">
    <img [src]="row.image" [alt]="row.name" class="product-image">
  </ng-template>

  <!-- Custom status template -->
  <ng-template #statusTemplate let-row="row">
    <span [class]="'status-badge status-' + row.status.toLowerCase()">
      {{ row.status }}
    </span>
  </ng-template>

  <!-- Custom actions template -->
  <ng-template #actionsTemplate let-row="row">
    <button mat-icon-button (click)="editProduct(row)" aria-label="Edit">
      <mat-icon>edit</mat-icon>
    </button>
    <button mat-icon-button (click)="deleteProduct(row)" aria-label="Delete">
      <mat-icon>delete</mat-icon>
    </button>
  </ng-template>
</app-data-table>
```

#### With Reactive Forms for Filtering
```typescript
export class FilteredDataComponent implements OnInit {
  data: any[] = [];
  filteredData: any[] = [];
  filterForm: FormGroup;

  columns = [
    { key: 'name', label: 'Name', sortable: true, filterable: true },
    { key: 'category', label: 'Category', filterable: true },
    { key: 'date', label: 'Date', sortable: true, pipe: 'date' }
  ];

  constructor(private fb: FormBuilder) {
    this.filterForm = this.fb.group({
      name: [''],
      category: [''],
      dateFrom: [''],
      dateTo: ['']
    });
  }

  ngOnInit(): void {
    this.loadData();
    this.setupFilters();
  }

  private setupFilters(): void {
    this.filterForm.valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged()
    ).subscribe(filters => {
      this.applyFilters(filters);
    });
  }

  private applyFilters(filters: any): void {
    this.filteredData = this.data.filter(item => {
      return (!filters.name || item.name.toLowerCase().includes(filters.name.toLowerCase())) &&
             (!filters.category || item.category === filters.category) &&
             (!filters.dateFrom || new Date(item.date) >= new Date(filters.dateFrom)) &&
             (!filters.dateTo || new Date(item.date) <= new Date(filters.dateTo));
    });
  }

  onFilterChange(event: FilterEvent): void {
    // Handle table filter changes
    this.filterForm.patchValue({ [event.column]: event.value });
  }
}
```

### Styling

#### Component Styles
```scss
.data-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid var(--table-border-color);
  background: var(--table-background);

  &__header {
    background: var(--table-header-background);
    border-bottom: 2px solid var(--table-border-color);

    th {
      padding: var(--table-cell-padding);
      text-align: left;
      font-weight: 600;
      user-select: none;

      &.sortable {
        cursor: pointer;
        
        &:hover {
          background: var(--table-header-hover);
        }
      }

      .sort-indicator {
        margin-left: 8px;
        opacity: 0.5;

        &.active {
          opacity: 1;
        }
      }
    }
  }

  &__body {
    tr {
      border-bottom: 1px solid var(--table-border-color);
      transition: background-color 0.2s ease;

      &:hover {
        background: var(--table-row-hover);
      }

      &.selected {
        background: var(--table-row-selected);
      }

      &.clickable {
        cursor: pointer;
      }
    }

    td {
      padding: var(--table-cell-padding);
      vertical-align: middle;

      &.text-center { text-align: center; }
      &.text-right { text-align: right; }
    }
  }

  &__loading {
    text-align: center;
    padding: 40px;
    color: var(--text-muted);
  }

  &__empty {
    text-align: center;
    padding: 40px;
    color: var(--text-muted);
    font-style: italic;
  }
}

.table-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  gap: 16px;

  &__search {
    flex: 1;
    max-width: 300px;
  }

  &__actions {
    display: flex;
    gap: 8px;
  }
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 16px;
  gap: 8px;
}

// Responsive design
@media (max-width: 768px) {
  .data-table {
    font-size: 14px;

    &__header th,
    &__body td {
      padding: 8px 4px;
    }
  }

  .table-controls {
    flex-direction: column;
    align-items: stretch;
  }
}
```

#### CSS Custom Properties
```scss
.data-table {
  --table-border-color: #e0e0e0;
  --table-background: white;
  --table-header-background: #f8f9fa;
  --table-header-hover: #e9ecef;
  --table-row-hover: #f8f9fa;
  --table-row-selected: #e3f2fd;
  --table-cell-padding: 12px 16px;
  --text-muted: #6c757d;
}
```

### Accessibility

- **ARIA Labels**: Table has proper `role="table"` and column headers
- **Keyboard Navigation**: Support for Tab, Enter, Space, and Arrow keys
- **Screen Reader**: Announces sort state and selection changes
- **Focus Management**: Clear focus indicators and logical tab order
- **High Contrast**: Supports high contrast mode

#### Accessibility Implementation
```html
<table 
  class="data-table" 
  role="table" 
  [attr.aria-label]="'Data table with ' + data.length + ' rows'">
  
  <thead role="rowgroup">
    <tr role="row">
      <th 
        *ngFor="let column of columns"
        role="columnheader"
        [attr.aria-sort]="getSortState(column.key)"
        [attr.aria-label]="getColumnAriaLabel(column)"
        (click)="sort(column.key)"
        (keydown.enter)="sort(column.key)"
        (keydown.space)="sort(column.key)"
        tabindex="0">
        {{ column.label }}
      </th>
    </tr>
  </thead>
  
  <tbody role="rowgroup">
    <tr 
      *ngFor="let row of paginatedData; trackBy: trackByFn"
      role="row"
      [attr.aria-selected]="isSelected(row)"
      (click)="selectRow(row)">
      <td 
        *ngFor="let column of columns"
        role="gridcell"
        [attr.aria-label]="getCellAriaLabel(row, column)">
        <!-- Cell content -->
      </td>
    </tr>
  </tbody>
</table>
```

### Testing

#### Component Tests
```typescript
describe('DataTableComponent', () => {
  let component: DataTableComponent<any>;
  let fixture: ComponentFixture<DataTableComponent<any>>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DataTableComponent],
      imports: [CommonModule, FormsModule]
    });

    fixture = TestBed.createComponent(DataTableComponent);
    component = fixture.componentInstance;
  });

  it('should render data correctly', () => {
    const testData = [
      { id: 1, name: 'Test Item 1' },
      { id: 2, name: 'Test Item 2' }
    ];
    const testColumns = [
      { key: 'id', label: 'ID' },
      { key: 'name', label: 'Name' }
    ];

    component.data = testData;
    component.columns = testColumns;
    fixture.detectChanges();

    const rows = fixture.debugElement.queryAll(By.css('tbody tr'));
    expect(rows.length).toBe(2);
  });

  it('should emit rowClick event', () => {
    spyOn(component.rowClick, 'emit');
    const testRow = { id: 1, name: 'Test' };

    component.onRowClick(testRow);

    expect(component.rowClick.emit).toHaveBeenCalledWith(testRow);
  });

  it('should sort data correctly', () => {
    component.data = [
      { id: 2, name: 'B' },
      { id: 1, name: 'A' }
    ];
    component.columns = [{ key: 'name', label: 'Name', sortable: true }];

    component.sort('name');
    fixture.detectChanges();

    expect(component.sortedData[0].name).toBe('A');
    expect(component.sortedData[1].name).toBe('B');
  });
});
```

### Performance Notes

- Uses `trackBy` functions for efficient list rendering
- Virtual scrolling support for large datasets
- OnPush change detection strategy
- Lazy loading for paginated data
- Debounced filtering to prevent excessive API calls

### Notes

- Component supports generic typing for type safety
- Integrates with Angular Material for consistent UI
- Supports internationalization (i18n)
- Compatible with Angular 12+ and Ivy renderer
- Responsive design with mobile-first approach
```

---

This comprehensive component documentation template covers the major frontend frameworks and provides detailed examples for different types of components. Adapt the sections and examples to match your specific component library and documentation needs.