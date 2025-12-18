<template>
  <div class="products">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-800">Product Management</h1>
      <p class="text-gray-600 mt-2">Manage your inventory products and stock levels</p>
    </div>
    
    <!-- Search and Filter Bar -->
    <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-4 mb-6">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div class="flex-1">
          <div class="relative">
            <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            <input 
              type="text" 
              placeholder="Search products by name, SKU, or category..." 
              class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
            >
          </div>
        </div>
        <div class="flex items-center space-x-3">
          <select class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
            <option>All Categories</option>
            <option>Electronics</option>
            <option>Accessories</option>
            <option>Components</option>
          </select>
          <select class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
            <option>All Status</option>
            <option>In Stock</option>
            <option>Low Stock</option>
            <option>Out of Stock</option>
          </select>
          <button class="px-4 py-2 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-lg hover:from-blue-700 hover:to-blue-800 transition-all flex items-center shadow-md">
            <i class="fas fa-plus mr-2"></i>
            Add Product
          </button>
        </div>
      </div>
    </div>
    
    <!-- Products Table -->
    <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gradient-to-r from-gray-50 to-gray-100">
            <tr>
              <th class="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                <div class="flex items-center">
                  <input type="checkbox" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
                  <span class="ml-3">Product</span>
                </div>
              </th>
              <th class="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">SKU</th>
              <th class="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Category</th>
              <th class="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Stock</th>
              <th class="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Price</th>
              <th class="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Status</th>
              <th class="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="product in products" :key="product.id" class="hover:bg-gray-50 transition">
              <td class="px-6 py-4">
                <div class="flex items-center">
                  <input type="checkbox" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
                  <div class="ml-4">
                    <div class="flex items-center">
                      <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center mr-3">
                        <i :class="`fas fa-${product.icon} text-gray-600`"></i>
                      </div>
                      <div>
                        <div class="text-sm font-medium text-gray-900">{{ product.name }}</div>
                        <div class="text-xs text-gray-500">{{ product.description }}</div>
                      </div>
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-mono text-gray-900">{{ product.sku }}</div>
                <div class="text-xs text-gray-500">Location: {{ product.location }}</div>
              </td>
              <td class="px-6 py-4">
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                  {{ product.category }}
                </span>
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-gray-900">{{ product.stock }} units</div>
                <div class="w-24 bg-gray-200 rounded-full h-1.5 mt-1">
                  <div 
                    :class="`h-1.5 rounded-full ${product.stockLevel}`"
                    :style="{ width: `${(product.stock / 100) * 100}%` }"
                  ></div>
                </div>
              </td>
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-gray-900">{{ product.price }}</div>
                <div class="text-xs text-gray-500">Value: {{ product.value }}</div>
              </td>
              <td class="px-6 py-4">
                <span :class="`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${product.statusClass}`">
                  <i :class="`fas fa-circle mr-1 ${product.statusIcon}`" style="font-size: 6px"></i>
                  {{ product.status }}
                </span>
              </td>
              <td class="px-6 py-4">
                <div class="flex items-center space-x-2">
                  <button class="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition" title="Edit">
                    <i class="fas fa-edit"></i>
                  </button>
                  <button class="p-2 text-green-600 hover:bg-green-50 rounded-lg transition" title="Stock In">
                    <i class="fas fa-arrow-down"></i>
                  </button>
                  <button class="p-2 text-red-600 hover:bg-red-50 rounded-lg transition" title="Stock Out">
                    <i class="fas fa-arrow-up"></i>
                  </button>
                  <button class="p-2 text-gray-600 hover:bg-gray-50 rounded-lg transition" title="More">
                    <i class="fas fa-ellipsis-v"></i>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <!-- Empty State -->
      <div v-if="products.length === 0" class="py-16 text-center">
        <div class="w-20 h-20 mx-auto bg-gray-100 rounded-full flex items-center justify-center mb-4">
          <i class="fas fa-box-open text-3xl text-gray-400"></i>
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No products found</h3>
        <p class="text-gray-500 mb-6">Get started by adding your first product to inventory</p>
        <button class="px-6 py-3 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-lg hover:from-blue-700 hover:to-blue-800 transition-all flex items-center mx-auto shadow-md">
          <i class="fas fa-plus mr-2"></i>
          Add Your First Product
        </button>
      </div>
      
      <!-- Table Footer -->
      <div class="px-6 py-4 border-t border-gray-200">
        <div class="flex items-center justify-between">
          <div class="text-sm text-gray-500">
            Showing <span class="font-medium">1</span> to <span class="font-medium">8</span> of <span class="font-medium">24</span> products
          </div>
          <div class="flex items-center space-x-2">
            <button class="px-3 py-1 border border-gray-300 rounded-lg text-sm hover:bg-gray-50 transition">
              Previous
            </button>
            <button class="px-3 py-1 bg-blue-600 text-white rounded-lg text-sm hover:bg-blue-700 transition">
              1
            </button>
            <button class="px-3 py-1 border border-gray-300 rounded-lg text-sm hover:bg-gray-50 transition">
              2
            </button>
            <button class="px-3 py-1 border border-gray-300 rounded-lg text-sm hover:bg-gray-50 transition">
              3
            </button>
            <button class="px-3 py-1 border border-gray-300 rounded-lg text-sm hover:bg-gray-50 transition">
              Next
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Products',
  data() {
    return {
      products: [
        {
          id: 1,
          name: 'MacBook Pro 16"',
          description: 'Apple M3 Max, 64GB RAM',
          icon: 'laptop',
          sku: 'MBP-2024-001',
          category: 'Electronics',
          location: 'A-12',
          stock: 45,
          stockLevel: 'bg-green-500',
          price: '$2,499',
          value: '$112,455',
          status: 'In Stock',
          statusClass: 'bg-green-100 text-green-800',
          statusIcon: 'text-green-500'
        },
        {
          id: 2,
          name: 'iPhone 15 Pro',
          description: '256GB, Titanium',
          icon: 'mobile-alt',
          sku: 'IP15-PRO-001',
          category: 'Electronics',
          location: 'B-07',
          stock: 12,
          stockLevel: 'bg-green-500',
          price: '$999',
          value: '$11,988',
          status: 'In Stock',
          statusClass: 'bg-green-100 text-green-800',
          statusIcon: 'text-green-500'
        },
        {
          id: 3,
          name: 'AirPods Pro',
          description: '2nd Generation',
          icon: 'headphones',
          sku: 'AP-PRO-002',
          category: 'Accessories',
          location: 'C-03',
          stock: 8,
          stockLevel: 'bg-yellow-500',
          price: '$249',
          value: '$1,992',
          status: 'Low Stock',
          statusClass: 'bg-yellow-100 text-yellow-800',
          statusIcon: 'text-yellow-500'
        },
        {
          id: 4,
          name: 'USB-C Hub',
          description: '7-in-1 Adapter',
          icon: 'plug',
          sku: 'HUB-7IN1-001',
          category: 'Accessories',
          location: 'D-15',
          stock: 0,
          stockLevel: 'bg-red-500',
          price: '$89',
          value: '$0',
          status: 'Out of Stock',
          statusClass: 'bg-red-100 text-red-800',
          statusIcon: 'text-red-500'
        }
      ]
    }
  }
}
</script>