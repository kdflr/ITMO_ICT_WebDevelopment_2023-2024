<template>
      <div class="register-container">
        <form @submit.prevent="register" class="register-form">

          <h2>Register</h2>
          <div class="form-group">
            <label for="registerUsername">Username:</label>
            <input v-model="username" type="text" id="registerUsername" required />
          </div>
          <div class="form-group">
            <label for="registerEmail">Email:</label>
            <input v-model="email" type="email" id="registerEmail" required />
          </div>
          <div class="form-group">
            <label for="registerPassword">Password:</label>
            <input v-model="password" type="password" id="registerPassword" required />
          </div>
          <div class="form-group">
            <label for="registerRePassword">Repeat Password:</label>
            <input v-model="rePassword" type="password" id="registerRePassword" required />
          </div>
          <button type="submit">Register</button>
          <p class="login-link">Already have an account? <router-link to="/login">Login</router-link></p>
        </form>
      </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      rePassword: ''
    };
  },
  methods: {
    register() {
      if (this.password !== this.rePassword) {
        console.error('Passwords do not match');
        return;
      }
      axios.post('http://localhost:8000/aviation_app/auth/users/', {
        username: this.username,
        email: this.email,
        password: this.password,
        re_password: this.rePassword
      })
      .then(response => {
        console.log(response.data);
        this.$router.push({  path: `auth/profile/:id` });
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
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #fff;
}
.register-form {
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
  background-color: #4c98af;
  color: #fff;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  width: 100%;
}
button:hover {
  background-color: #457da0;
}
.login-link {
  text-align: center;
  margin-top: 10px;
}
.login-link a {
  color: #4c95af;
  text-decoration: none;
}
</style>