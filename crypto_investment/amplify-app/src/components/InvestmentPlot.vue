<template>
  <div>
    <h1>Investment Value Over Time</h1>
    <img :src="imageUrl" alt="Investment Plot" v-if="imageUrl">
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import { getUrl } from 'aws-amplify/storage';

export default {
  data() {
    return {
      imageUrl: null
    };
  },
  async mounted() {
    try {
      const getUrlResult = await getUrl({
        path: 'investment_plot.png',
        options: {
          validateObjectExistence: false,
          expiresIn: 900,
          useAccelerateEndpoint: false
        }
      });
      this.imageUrl = getUrlResult.url;
      console.log('signed URL: ', getUrlResult.url);
      console.log('URL expires at: ', getUrlResult.expiresAt);
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
