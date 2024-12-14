<template>
  <div class="navbar bg-base-100">
    <div class="navbar-start">
      <!-- 移动端的菜单按钮 -->
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" />
          </svg>
        </div>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li><RouterLink to="/view" class="text-lg font-medium">首页</RouterLink></li>
          <li><RouterLink to="/user" class="text-lg font-medium">用户管理</RouterLink></li>
          <li><RouterLink to="/car" class="text-lg font-medium">车辆管理</RouterLink></li>
          <li><RouterLink to="/record" class="text-lg font-medium">车流管理</RouterLink></li>
        </ul>
      </div>
      <!-- Logo和首页链接 -->
      <RouterLink to="/view" class="btn btn-ghost text-xl flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="iconify iconify--logos" width="40" height="40" preserveAspectRatio="xMidYMid meet" viewBox="0 0 64 64">
          <defs>
            <linearGradient id="Gradient5" x1="0%" x2="100%" y1="0%" y2="100%">
              <stop offset="0%" stop-color="#FF00FF"></stop>
              <stop offset="100%" stop-color="#00FFFF"></stop>
            </linearGradient>
          </defs>
          <circle cx="32" cy="32" r="20" fill="url(#Gradient5)" stroke="#FFF" stroke-width="4"/>
          <circle cx="32" cy="32" r="10" fill="none" stroke="#FFF" stroke-width="2"/>
          <path fill="none" stroke="#FFF" stroke-width="2" d="M32 12v40M12 32h40"/>
        </svg>
        泊云智停
      </RouterLink>
    </div>
    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li><RouterLink to="/view" class="text-lg font-medium">首页</RouterLink></li>
        <li><RouterLink to="/user" class="text-lg font-medium">用户管理</RouterLink></li>
        <li><RouterLink to="/car" class="text-lg font-medium">车辆管理</RouterLink></li>
        <li><RouterLink to="/record" class="text-lg font-medium">车流管理</RouterLink></li>
      </ul>
    </div>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  name: "Navbar",
}
</script>

<style>
/* 如果需要，你可以添加自定义的CSS样式 */
</style>
