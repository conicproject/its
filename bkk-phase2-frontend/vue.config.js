module.exports = {
  transpileDependencies: ["vuetify"],

  devServer: {
    host: '0.0.0.0',
    port: 8088,
    allowedHosts: 'all',
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    client: {
      webSocketURL: 'ws://security65.dyndns.org:8088/ws',
    }
  }
}
