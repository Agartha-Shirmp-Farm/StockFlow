<template>
  <div class="dashboard">
    <!-- Header -->
    <div class="mb-8">
      <div class="flex flex-col md:flex-row md:items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold text-gray-800">Dashboard Overview</h1>
          <p class="text-gray-600 mt-2">Welcome back! Here's what's happening with your inventory today.</p>
        </div>
        <div class="mt-4 md:mt-0 flex items-center space-x-2 text-sm">
          <span class="text-gray-500">Last updated:</span>
          <span class="font-medium">Just now</span>
          <button class="ml-2 p-2 hover:bg-gray-100 rounded-lg transition">
            <i class="fas fa-sync-alt"></i>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Stats Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <!-- Total Products Card -->
      <div class="bg-gradient-to-br from-white to-blue-50 rounded-xl shadow-lg border border-blue-100 p-6 transition-transform hover:scale-[1.02] duration-200">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-blue-600">Total Products</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">24</p>
            <div class="flex items-center mt-2">
              <span class="text-sm text-green-600 font-medium flex items-center">
                <i class="fas fa-arrow-up mr-1"></i> 12%
              </span>
              <span class="text-sm text-gray-500 ml-2">from last month</span>
            </div>
          </div>
          <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
            <i class="fas fa-boxes text-2xl text-blue-600"></i>
          </div>
        </div>
      </div>
      
      <!-- Low Stock Card -->
      <div class="bg-gradient-to-br from-white to-yellow-50 rounded-xl shadow-lg border border-yellow-100 p-6 transition-transform hover:scale-[1.02] duration-200">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-yellow-600">Low Stock Items</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">3</p>
            <div class="flex items-center mt-2">
              <span class="text-sm text-red-600 font-medium flex items-center">
                <i class="fas fa-exclamation-triangle mr-1"></i> Attention needed
              </span>
            </div>
          </div>
          <div class="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
            <i class="fas fa-exclamation-triangle text-2xl text-yellow-600"></i>
          </div>
        </div>
      </div>
      
      <!-- Today's Transactions -->
      <div class="bg-gradient-to-br from-white to-green-50 rounded-xl shadow-lg border border-green-100 p-6 transition-transform hover:scale-[1.02] duration-200">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-green-600">Today's Transactions</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">8</p>
            <div class="flex items-center mt-2">
              <span class="text-sm text-green-600 font-medium flex items-center">
                <i class="fas fa-exchange-alt mr-1"></i> Active
              </span>
            </div>
          </div>
          <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
            <i class="fas fa-exchange-alt text-2xl text-green-600"></i>
          </div>
        </div>
      </div>
      
      <!-- Total Value -->
      <div class="bg-gradient-to-br from-white to-purple-50 rounded-xl shadow-lg border border-purple-100 p-6 transition-transform hover:scale-[1.02] duration-200">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-purple-600">Inventory Value</p>
            <p class="text-3xl font-bold text-gray-800 mt-2">$12,450</p>
            <div class="flex items-center mt-2">
              <span class="text-sm text-purple-600 font-medium flex items-center">
                <i class="fas fa-chart-line mr-1"></i> +5.2%
              </span>
              <span class="text-sm text-gray-500 ml-2">growth</span>
            </div>
          </div>
          <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
            <i class="fas fa-dollar-sign text-2xl text-purple-600"></i>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Quick Actions & Chart -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
      <!-- Quick Actions -->
      <div class="lg:col-span-2 bg-white rounded-xl shadow-lg border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-xl font-semibold text-gray-800">Quick Actions</h2>
          <span class="text-sm text-gray-500">Frequent operations</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
          <button class="group flex flex-col items-center p-4 bg-gradient-to-br from-blue-50 to-blue-100 border border-blue-200 rounded-xl hover:border-blue-300 transition-all duration-200">
            <div class="w-12 h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
              <i class="fas fa-plus text-white text-xl"></i>
            </div>
            <span class="font-medium text-gray-800">Add Product</span>
            <span class="text-xs text-gray-600 mt-1">New item</span>
          </button>
          
          <button class="group flex flex-col items-center p-4 bg-gradient-to-br from-green-50 to-green-100 border border-green-200 rounded-xl hover:border-green-300 transition-all duration-200">
            <div class="w-12 h-12 bg-gradient-to-r from-green-500 to-green-600 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
              <i class="fas fa-arrow-down text-white text-xl"></i>
            </div>
            <span class="font-medium text-gray-800">Stock In</span>
            <span class="text-xs text-gray-600 mt-1">Receive items</span>
          </button>
          
          <button class="group flex flex-col items-center p-4 bg-gradient-to-br from-red-50 to-red-100 border border-red-200 rounded-xl hover:border-red-300 transition-all duration-200">
            <div class="w-12 h-12 bg-gradient-to-r from-red-500 to-red-600 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
              <i class="fas fa-arrow-up text-white text-xl"></i>
            </div>
            <span class="font-medium text-gray-800">Stock Out</span>
            <span class="text-xs text-gray-600 mt-1">Dispatch items</span>
          </button>
          
          <button class="group flex flex-col items-center p-4 bg-gradient-to-br from-purple-50 to-purple-100 border border-purple-200 rounded-xl hover:border-purple-300 transition-all duration-200">
            <div class="w-12 h-12 bg-gradient-to-r from-purple-500 to-purple-600 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
              <i class="fas fa-chart-bar text-white text-xl"></i>
            </div>
            <span class="font-medium text-gray-800">View Reports</span>
            <span class="text-xs text-gray-600 mt-1">Analytics</span>
          </button>
        </div>
      </div>
      
      <!-- Stock Status -->
      <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
        <h2 class="text-xl font-semibold text-gray-800 mb-6">Stock Status</h2>
        <div class="space-y-4">
          <div>
            <div class="flex justify-between text-sm mb-1">
              <span class="text-gray-700">In Stock</span>
              <span class="font-medium">18 items</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-2">
              <div class="bg-green-500 h-2 rounded-full" style="width: 75%"></div>
            </div>
          </div>
          <div>
            <div class="flex justify-between text-sm mb-1">
              <span class="text-gray-700">Low Stock</span>
              <span class="font-medium">3 items</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-2">
              <div class="bg-yellow-500 h-2 rounded-full" style="width: 12.5%"></div>
            </div>
          </div>
          <div>
            <div class="flex justify-between text-sm mb-1">
              <span class="text-gray-700">Out of Stock</span>
              <span class="font-medium">3 items</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-2">
              <div class="bg-red-500 h-2 rounded-full" style="width: 12.5%"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Recent Activity -->
    <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-xl font-semibold text-gray-800">Recent Activity</h2>
        <button class="text-sm text-blue-600 hover:text-blue-700 font-medium flex items-center">
          <span>View All</span>
          <i class="fas fa-arrow-right ml-1"></i>
        </button>
      </div>
      
      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead>
            <tr class="bg-gray-50">
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Time</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Activity</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Product</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
              <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="(activity, index) in recentActivities" :key="index" class="hover:bg-gray-50 transition">
              <td class="px-4 py-3 whitespace-nowrap">
                <div class="text-sm text-gray-900">{{ activity.time }}</div>
                <div class="text-xs text-gray-500">{{ activity.date }}</div>
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center">
                  <div :class="`w-8 h-8 rounded-full ${activity.iconBg} flex items-center justify-center mr-3`">
                    <i :class="`fas fa-${activity.icon} ${activity.iconColor}`"></i>
                  </div>
                  <span class="text-sm font-medium text-gray-900">{{ activity.action }}</span>
                </div>
              </td>
              <td class="px-4 py-3">
                <div class="text-sm text-gray-900">{{ activity.product }}</div>
                <div class="text-xs text-gray-500">SKU: {{ activity.sku }}</div>
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center">
                  <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center text-xs text-blue-600 mr-2">
                    {{ activity.user.initials }}
                  </div>
                  <span class="text-sm text-gray-900">{{ activity.user.name }}</span>
                </div>
              </td>
              <td class="px-4 py-3">
                <span :class="`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${activity.statusClass}`">
                  {{ activity.status }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      recentActivities: [
        {
          time: '10:30 AM',
          date: 'Today',
          icon: 'arrow-down',
          iconBg: 'bg-green-100',
          iconColor: 'text-green-600',
          action: 'Stock In',
          product: 'MacBook Pro 16"',
          sku: 'MBP-2024-001',
          user: { initials: 'JD', name: 'John Doe' },
          status: 'Completed',
          statusClass: 'bg-green-100 text-green-800'
        },
        {
          time: '09:15 AM',
          date: 'Today',
          icon: 'arrow-up',
          iconBg: 'bg-red-100',
          iconColor: 'text-red-600',
          action: 'Stock Out',
          product: 'iPhone 15 Pro',
          sku: 'IP15-001',
          user: { initials: 'AS', name: 'Alex Smith' },
          status: 'Pending',
          statusClass: 'bg-yellow-100 text-yellow-800'
        },
        {
          time: 'Yesterday',
          date: '4:45 PM',
          icon: 'plus',
          iconBg: 'bg-blue-100',
          iconColor: 'text-blue-600',
          action: 'New Product',
          product: 'AirPods Pro',
          sku: 'AP-PRO-002',
          user: { initials: 'MJ', name: 'Maria Johnson' },
          status: 'Completed',
          statusClass: 'bg-green-100 text-green-800'
        }
      ]
    }
  }
}
</script>