import { createApp } from 'vue';
import App from './App.vue';
import { Amplify } from 'aws-amplify'

import awsconfig from './aws-exports'; // This file is generated by Amplify and contains your configuration

Amplify.configure(awsconfig);



createApp(App).mount('#app');
