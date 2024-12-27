In Next.js 14, the `getStaticProps` function is not supported in the `app` directory. This means that if you're using the `app` directory for routing, you'll need to use other methods for data fetching. Two such methods are `getServerSideProps` for server-side rendering and SWR for client-side data fetching.

## Server-Side Rendering with `getServerSideProps`

The `getServerSideProps` function is used for server-side rendering in Next.js. It fetches data on each request, making it suitable for pages that need to display frequently updated data. Here's an example of how you might use `getServerSideProps`:

```javascript
export async function getServerSideProps(context) {
  const res = await fetch(`https://api.example.com/data/${context.params.id}`)
  const data = await res.json()

  return {
    props: {
      data,
    },
  }
}
```

In this example, `getServerSideProps` fetches data based on the `id` parameter from the current URL. The fetched data is then passed as a prop to the React component for that page [11, {ts:2}][15, {ts:6}][24, {ts:10}].

## Client-Side Data Fetching with SWR

SWR is a React Hooks library for data fetching. It stands for "stale-while-revalidate", a cache invalidation strategy. Here's an example of how you might use SWR in a Next.js application:

```javascript
import useSWR from 'swr'

function Profile() {
  const { data, error } = useSWR('/api/user', fetch)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return <div>Hello {data.name}!</div>
}
```

In this example, the `useSWR` hook fetches data from the `/api/user` endpoint. While the data is being fetched, it displays "Loading...". If there's an error in fetching the data, it displays "Failed to load". Once the data has been fetched, it displays a greeting with the user's name [4, {ts:4}][8, {ts:0}][12].

Remember, these are just examples. The actual implementation will depend on the specifics of your application and the data you're working with.

