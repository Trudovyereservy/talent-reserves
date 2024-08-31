/** @type {import('next').NextConfig} */
const nextConfig = {
    eslint: {
      ignoreDuringBuilds: true,
    },
    output: 'standalone',
    images: {
        domains: ['talent-reserves.storage.yandexcloud.net', 'localhost:3000', '127.0.0.1:3000'],
      },
}

module.exports = nextConfig
