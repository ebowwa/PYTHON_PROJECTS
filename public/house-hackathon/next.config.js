/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => {
    return [
      {
        source: '/api/:path*',
        destination:
          process.env.NODE_ENV === 'development'
            ? 'https://house-hackathon-git-main-ebowwa.vercel.app/api/:path*'
            : '/api/',
      },
    ]
  },
}

module.exports = nextConfig
