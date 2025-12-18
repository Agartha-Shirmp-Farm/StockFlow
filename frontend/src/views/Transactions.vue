<template>
  <div class="transactions">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-800">Transaction History</h1>
      <p class="text-gray-600 mt-2">Track all inventory movements and transactions</p>
    </div>
    
    <!-- Transaction Stats -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
      <div class="bg-gradient-to-br from-blue-50 to-blue-100 border border-blue-200 rounded-xl p-4">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-blue-700">Total Transactions</p>
            <p class="text-2xl font-bold text-gray-800 mt-1">156</p>
          </div>
          <i class="fas fa-exchange-alt text-2xl text-blue-500"></i>
        </div>
      </div>
      <div class