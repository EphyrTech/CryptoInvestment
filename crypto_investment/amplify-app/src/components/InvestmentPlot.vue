<template>
  <div>
    <h1>Investment Value Over Time</h1>
    <line-chart :chart-data="chartData" :options="chartOptions"></line-chart>
  </div>
</template>

<script>
import { DataStore } from 'aws-amplify';
import { CryptoPrice } from '@/models'; // Ensure this path is correct
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

export default {
  components: {
    LineChart: Line
  },
  data() {
    return {
      models: [],
      chartData: {
        labels: [],
        datasets: []
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  async mounted() {
    try {
      const models = await DataStore.query(CryptoPrice);
      this.models = models;
      this.updateChartData();
      console.log(models);
    } catch (error) {
      console.error('Error querying DataStore:', error);
    }
  },
  methods: {
    updateChartData() {
      const labels = [];
      const coinData = {};

      // Prepare the data structure
      this.models.forEach(model => {
        if (!labels.includes(model.Date)) {
          labels.push(model.Date);
        }
        if (!coinData[model.Coin]) {
          coinData[model.Coin] = [];
        }
      });

      // Populate the data for each coin
      labels.sort(); // Ensure labels are sorted by date
      Object.keys(coinData).forEach(coin => {
        labels.forEach(label => {
          const priceRecord = this.models.find(model => model.Date === label && model.Coin === coin);
          coinData[coin].push(priceRecord ? priceRecord.Price : null);
        });
      });

      // Create datasets for the chart
      const datasets = Object.keys(coinData).map(coin => ({
        label: coin,
        data: coinData[coin],
        borderColor: this.getRandomColor(),
        backgroundColor: 'rgba(0, 0, 0, 0.1)'
      }));

      this.chartData = {
        labels,
        datasets
      };
    },
    getRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
  }
};
</script>

<style scoped>
.chart-container {
  position: relative;
  margin: auto;
  height: 40vh;
  width: 80vw;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 5px;
  border-bottom: 1px solid #ccc;
}
</style>
