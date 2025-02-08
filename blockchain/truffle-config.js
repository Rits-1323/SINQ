const path = require('path');

module.exports = {
  // Define the networks configuration
  networks: {
    development: {
      host: "127.0.0.1", // Localhost
      port: 8545,        // Standard Ethereum port
      network_id: "*",   // Match any network id
      gas: 6721975,      // Gas limit
      gasPrice: 20000000000,  // 20 Gwei
    },
  },

  // Define the compilers configuration
  compilers: {
    solc: {
      version: "0.8.20",  // specify the correct version here
      settings: {
        optimizer: {
          enabled: true,
          runs: 200
        },
      },
    },
  },

  // Configure the contracts build folder
  contracts_build_directory: path.join(__dirname, "blockchain", "build"),

  // For testing: define mocha configuration
  mocha: {
    timeout: 100000,  // Max time for each test
  },

  // Plugins (optional, e.g., for coverage)
  plugins: [],

  // Configure deployment: optionally use Infura for testnets
  api_keys: {
    // For example, adding Infura key if you use it:
    infura: "<YOUR_INFURA_KEY>"
  },
};
