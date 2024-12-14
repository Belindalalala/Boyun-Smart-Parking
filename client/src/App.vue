<template>
  <div id="app">
    <!-- 如果用户已登录，显示导航栏和页面内容；否则显示登录页面 -->
    <div v-if="authState.isAuthenticated">
      <Navbar />
      <router-view></router-view>
    </div>
    <div v-else>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import { authState } from './authState'; // 引入登录状态

export default {
  components: {
    Navbar
  },
  computed: {
    authState() {
      return authState; // 将全局状态引入为计算属性
    }
  }
};
</script>
