<template>
  <div class="reports p-6">
    <h1 class="text-3xl font-bold mb-8 text-gray-800">Reports</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="bg-white p-6 rounded-lg shadow border border-gray-200">
        <h3 class="text-lg font-semibold mb-4">Stock Levels</h3>
        <div class="h-48 flex items-center justify-center text-gray-400">
          Chart will appear here
        </div>
      </div>
      
      <div class="bg-white p-6 rounded-lg shadow border border-gray-200">
        <h3 class="text-lg font-semibold mb-4">Transaction History</h3>
        <div class="h-48 flex items-center justify-center text-gray-400">
          Chart will appear here
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Reports'
}
</script>
