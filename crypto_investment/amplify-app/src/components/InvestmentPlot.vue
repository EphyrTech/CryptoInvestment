<template>
  <div>
    <h1>Investment Value Over Time</h1>
    <img :src="imageUrl" alt="Investment Plot" v-if="imageUrl">
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import { Storage } from 'aws-amplify';

export default {
  data() {
    return {
      imageUrl: null
    };
  },
  async mounted() {
    try {
      this.imageUrl = await Storage.get('investment_plot.png', {
        level: 'public' // Adjust based on your S3 bucket configuration
      });
    } catch (error) {
      console.error('Error fetching image from S3:', error);
    }
  }
};
</script>

<style scoped>
img {
  max-width: 100%;
  height: auto;
}
</style>
