
<template>
  <div>
    <h1>Investment Value Over Time</h1>
    <img :src="imageUrl" alt="Investment Plot">
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageUrl: 'https://crypto-visualizations.s3.amazonaws.com/investment_plot.png'
    };
  }
};
</script>

<style scoped>
img {
  max-width: 100%;
  height: auto;
}
</style>
