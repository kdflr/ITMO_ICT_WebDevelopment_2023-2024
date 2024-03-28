<template>
      <div class="login-container">
        <form @submit.prevent="login" class="login-form">
          <h2>Login</h2>
          <div class="form-group">
            <label for="loginUsername">Username:</label>
            <input v-model="username" type="text" id="loginUsername" required />
          </div>
          <div class="form-group">
            <label for="loginPassword">Password:</label>
            <input v-model="password" type="password" id="loginPassword" required />
          </div>
          <button type="submit">Login</button>
          <p class="register-link">No account? <router-link to="/register">Register</router-link></p>
        </form>
      </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      axios.post('http://localhost:8000/auth/login/', {
        username: this.username,
        password: this.password,
      })
      .then(response => {
        console.log('Server Response:', response.data);
        localStorage.setItem('token', response.data.token);
          const userId = response.data.id;
        console.log('User ID:', userId);
        console.log(response.data);
        this.$router.push({ path: `/auth/users/${userId}`});
      })
      .catch(error => {
        console.error(error);
      });
    }
  }
};
</script>
<style scoped>
.background-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
}
.login-form {
  max-width: 300px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
h2 {
  text-align: center;
  color: #4cafa7;
}
.form-group {
  margin-bottom: 15px;
}
label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}
input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
}
button {
  background-color: #4cafaf;
  color: #fff;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  width: 100%;
}
button:hover {
  background-color: #458ba0;
}
.register-link {
  text-align: center;
  margin-top: 10px;
}
.register-link a {
  color: #4cafa7;
  text-decoration: none;
}
</style>