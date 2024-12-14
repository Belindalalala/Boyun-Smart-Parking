// src/authState.js

import { reactive } from "vue";

// 全局认证状态
export const authState = reactive({
  isAuthenticated: false, // 用户是否已登录
});
