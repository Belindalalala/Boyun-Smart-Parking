<template>
  <div class="relative min-h-screen bg-base-200">
    <!-- 顶部导航 -->
    <nav class="flex justify-between items-center px-6 py-4 bg-base-100 shadow">
      <div class="flex items-center space-x-3">
        <!-- 图标 -->
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
        <!-- 标题 -->
        <span class="text-xl font-bold">泊云智停</span>
      </div>
      <!-- 主题切换按钮 -->
      <label class="swap swap-rotate">
        <!-- 隐藏的 checkbox 控制状态 -->
        <input
          type="checkbox"
          class="theme-toggle"
          @click="setDataTheme"
        />
        <!-- 太阳图标 -->
        <svg
          class="swap-on fill-current w-6 h-6"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
        >
          <path
            d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z"
          />
        </svg>
        <!-- 月亮图标 -->
        <svg
          class="swap-off fill-current w-6 h-6"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
        >
          <path
            d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z"
          />
        </svg>
      </label>
    </nav>

    <!-- 主体内容 -->
    <main class="mx-auto text-center mt-10">
      <form @submit.prevent="handleLogin">
        <div class="form-control w-full max-w-xs mx-auto text-center">
          <label class="label">
            <span class="label-text">请输入您的姓名</span>
          </label>
          <input
            v-model="username"
            type="text"
            placeholder="输入姓名"
            class="input input-bordered w-full max-w-xs"
            required
          />
        </div>
        <div class="form-control w-full max-w-xs mx-auto text-center mt-4">
          <label class="label">
            <span class="label-text">设置您的密码</span>
          </label>
          <input
            v-model="password"
            type="password"
            placeholder="输入密码"
            class="input input-bordered w-full max-w-xs"
            required
          />
        </div>
        <div class="form-control w-full max-w-xs mx-auto text-center mt-4">
          <label class="label">
            <span class="label-text">请输入额外信息</span>
          </label>
          <input
            v-model="value"
            type="text"
            placeholder="输入额外信息"
            class="input input-bordered w-full max-w-xs"
            required
          />
        </div>
        <br />
        <button class="btn btn-primary mt-4">登录</button>
      </form>
      <!-- 错误消息 -->
      <p v-if="errorMessage" class="text-red-500 mt-4">{{ errorMessage }}</p>
    </main>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref, watch } from "vue";
import { authState } from '../authState';

// 登录表单的数据
const username = ref('');
const password = ref('');
const value = ref('');
const errorMessage = ref('');

// 使用 router 进行页面跳转
const router = useRouter();

// 确保 CSRF Token 在请求头中发送
axios.defaults.xsrfCookieName = 'csrftoken';  // 默认值是 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken';  // 请求头中发送 CSRF Token

// 发送请求
const handleLogin = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/login/', {
      username: username.value,
      password: password.value,
      value: value.value,
    });

    const { token } = response.data;
    localStorage.setItem('auth_token', token);

    // 跳转到用户主页
    router.replace('/view');
    authState.isAuthenticated = true; // 设置认证状态为已登录

  } catch (error) {
    console.error('Login failed:', error);
    if (error.response) {
      errorMessage.value = error.response.data.detail || '登录失败，请检查用户名或密码';
    } else {
      errorMessage.value = '网络错误，请稍后重试';
    }
  }
};



// 当前主题状态
const dataTheme = ref("light");

// 切换主题函数
const setDataTheme = () => {
  dataTheme.value = dataTheme.value === "light" ? "dark" : "light";
};

// 监听主题变化并动态修改 <html> 标签属性
watch(dataTheme, (newTheme) => {
  document.documentElement.setAttribute("data-theme", newTheme);
});

// 初始化主题
document.documentElement.setAttribute("data-theme", dataTheme.value);


</script>
