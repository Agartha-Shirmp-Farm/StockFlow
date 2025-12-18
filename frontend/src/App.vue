<template>
  <div id="app" class="min-h-screen bg-gray-50">
    <!-- Enhanced Navigation -->
    <nav class="bg-gradient-to-r from-blue-600 to-indigo-700 text-white shadow-xl">
      <div class="container mx-auto px-4 py-3">
        <div class="flex items-center justify-between">
          <!-- Logo & Brand -->
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center shadow-md">
              <i class="fas fa-boxes text-xl"></i>
            </div>
            <div>
              <h1 class="text-xl font-bold tracking-tight">StockFlow</h1>
              <p class="text-xs text-blue-100 opacity-80">Inventory Management</p>
            </div>
          </div>
          
          <!-- Navigation Links -->
          <div class="hidden md:flex items-center space-x-1">
            <router-link 
              to="/" 
              class="flex items-center space-x-2 px-4 py-2 rounded-lg transition-all duration-200"
              :class="{
                'bg-white/20 shadow-inner': $route.path === '/',
                'hover:bg-white/10': $route.path !== '/'
              }"
            >
              <i class="fas fa-chart-line"></i>
              <span>Dashboard</span>
            </router-link>
            <router-link 
              to="/products" 
              class="flex items-center space-x-2 px-4 py-2 rounded-lg transition-all duration-200"
              :class="{
                'bg-white/20 shadow-inner': $route.path === '/products',
                'hover:bg-white/10': $route.path !== '/products'
              }"
            >
              <i class="fas fa-box"></i>
              <span>Products</span>
            </router-link>
            <router-link 
              to="/transactions" 
              class="flex items-center space-x-2 px-4 py-2 rounded-lg transition-all duration-200"
              :class="{
                'bg-white/20 shadow-inner': $route.path === '/transactions',
                'hover:bg-white/10': $route.path !== '/transactions'
              }"
            >
              <i class="fas fa-exchange-alt"></i>
              <span>Transactions</span>
            </router-link>
            <router-link 
              to="/reports" 
              class="flex items-center space-x-2 px-4 py-2 rounded-lg transition-all duration-200"
              :class="{
                'bg-white/20 shadow-inner': $route.path === '/reports',
                'hover:bg-white/10': $route.path !== '/reports'
              }"
            >
              <i class="fas fa-chart-bar"></i>
              <span>Reports</span>
            </router-link>
          </div>
          
          <!-- User Profile -->
          <div class="flex items-center space-x-4">
            <button class="relative p-2 hover:bg-white/10 rounded-lg transition">
              <i class="fas fa-bell"></i>
              <span class="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full"></span>
            </button>
            <div class="hidden md:flex items-center space-x-3 bg-white/10 backdrop-blur-sm rounded-xl px-4 py-2">
              <div class="w-8 h-8 bg-white rounded-full flex items-center justify-center">
                <i class="fas fa-user text-blue-600"></i>
              </div>
              <span class="font-medium">Admin</span>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Mobile Navigation -->
    <div class="md:hidden bg-white shadow-md">
      <div class="flex justify-around py-2">
        <router-link 
          to="/" 
          class="flex flex-col items-center p-2"
          :class="{ 'text-blue-600': $route.path === '/' }"
        >
          <i class="fas fa-chart-line mb-1"></i>
          <span class="text-xs">Dashboard</span>
        </router-link>
        <router-link 
          to="/products" 
          class="flex flex-col items-center p-2"
          :class="{ 'text-blue-600': $route.path === '/products' }"
        >
          <i class="fas fa-box mb-1"></i>
          <span class="text-xs">Products</span>
        </router-link>
        <router-link 
          to="/transactions" 
          class="flex flex-col items-center p-2"
          :class="{ 'text-blue-600': $route.path === '/transactions' }"
        >
          <i class="fas fa-exchange-alt mb-1"></i>
          <span class="text-xs">Transactions</span>
        </router-link>
        <router-link 
          to="/reports" 
          class="flex flex-col items-center p-2"
          :class="{ 'text-blue-600': $route.path === '/reports' }"
        >
          <i class="fas fa-chart-bar mb-1"></i>
          <span class="text-xs">Reports</span>
        </router-link>
      </div>
    </div>
    
    <!-- Main Content -->
    <main class="container mx-auto px-4 py-6">
      <div class="mb-6">
        <div class="text-sm text-gray-500 flex items-center space-x-2">
          <i class="fas fa-home"></i>
          <span>/</span>
          <span class="capitalize">{{ $route.name }}</span>
        </div>
      </div>
      <router-view />
    </main>
    
    <!-- Enhanced Footer -->
    <footer class="mt-auto border-t border-gray-200 bg-white py-6">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="mb-4 md:mb-0">
            <div class="flex items-center space-x-2">
              <div class="w-8 h-8 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
                <i class="fas fa-boxes text-white text-sm"></i>
              </div>
              <span class="font-bold text-gray-800">StockFlow</span>
            </div>
            <p class="text-sm text-gray-600 mt-2">Skibidi your inventory management</p>
          </div>
          
          <div class="flex items-center space-x-6">
            <a href="#" class="text-gray-600 hover:text-blue-600 transition">
              <i class="fab fa-github"></i>
            </a>
            <a href="#" class="text-gray-600 hover:text-blue-600 transition">
              <i class="fas fa-question-circle"></i>
            </a>
            <a href="#" class="text-gray-600 hover:text-blue-600 transition">
              <i class="fas fa-cog"></i>
            </a>
          </div>
        </div>
        <div class="mt-6 pt-6 border-t border-gray-100 text-center text-sm text-gray-500">
          <p class="mt-1">v2.0.0 • Built with Vue.js & Tailwind CSS</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
.router-link-exact-active {
  font-weight: 600;
}

/* Smooth transitions */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>