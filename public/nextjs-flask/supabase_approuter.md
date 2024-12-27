# supabase next.js app router 14ish
# To implement session management using cookies with Supabase in a Next.js App Router, you would need to follow these steps:

1. **Install Next.js Auth Helpers Library**: This library helps to configure Supabase Auth to store the user's session in a cookie instead of localStorage. This is important for server-side rendering and for the App Router to access the session on both the client and server sides.
2. **Declare Environment Variables**: You need to set up your environment variables by retrieving your project's URL and anon key from your Supabase API settings. These should be added to a `.env.local` file in your project.
3. **Managing Session with Middleware**: You will use middleware to refresh the user's session before loading Server Component routes. This ensures that the session is always up-to-date and valid for each request.
4. **Set Up App Router**: Configure the App Router to automatically send the session along with any requests to Supabase. This means that the session cookie will be included in the headers of each request, allowing Supabase to authenticate the user.

Here is a JavaScript code snippet that demonstrates how you might use middleware to manage sessions with cookies in a Next.js application:

```javascript
import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs';
import { NextResponse } from 'next/server';

export async function middleware(req) {
  const res = NextResponse.next();
  const supabase = createMiddlewareClient({ req, res });

  const { data: { session } } = await supabase.auth.getSession();

  if (!session && req.nextUrl.pathname.startsWith('/protected-route')) {
    // If there is no session and the user is trying to access a protected route,
    // redirect them to the sign-in page.
    const redirectUrl = req.nextUrl.clone();
    redirectUrl.pathname = '/sign-in';
    return NextResponse.redirect(redirectUrl);
  }

  // If there is a session, or the user is not accessing a protected route,
  // proceed with the request.
  return res;
}
```

In this example, `createMiddlewareClient` is used to create a Supabase client that can interact with the session cookie. The `getSession` method checks for an existing session, and if there isn't one (and the user is trying to access a protected route), it redirects them to a sign-in page. Otherwise, it allows the request to proceed.

To test if Supabase is using cookies for session management in a Next.js App Router, you can follow a systematic approach to verify the session's storage and management mechanism. This involves checking both the client-side and server-side behaviors to ensure that sessions are indeed being managed through cookies. Here's a detailed guide on how to perform this test:

### 1. Inspect Network Requests
First, you can inspect the network requests made from your Next.js application to the Supabase API. This can be done using the Developer Tools in your web browser (usually accessible by pressing F12 or right-clicking the page and selecting "Inspect").
- **Look for Authentication Requests**: Specifically, look for network requests related to authentication (e.g., sign-in, sign-up, token refresh).
- **Check Request Headers**: In the details of these requests, check the request headers for a `Cookie` header. This header should contain the session cookie if Supabase is configured to use cookies for session management.

### 2. Verify Cookie Presence in the Browser
- **Browser's Application/Storage Tab**: In the Developer Tools, navigate to the Application or Storage tab (the name might vary depending on the browser). Here, you can see all cookies set by your application.
- **Look for Supabase Session Cookies**: Check for cookies that are related to Supabase session management. These might be prefixed with `sb:` or have names related to authentication or sessions.

### 3. Check Server-Side Behavior
If you're using Next.js middleware or API routes to interact with Supabase, you can add logging to these server-side components to verify that the session is being retrieved from cookies.
- **Modify Middleware/API Routes**: Temporarily add `console.log` statements to your middleware or API routes where you interact with Supabase's session management functions. For example, log the result of `supabase.auth.getSession()` or any similar method you're using.
- **Check Server Logs**: When you make requests that hit these server-side components, check your server logs to see if the session information is being successfully retrieved from cookies.

### 4. Test Session Persistence
- **Session Persistence Across Requests**: Perform actions in your application that require authentication and navigate across different routes. If your session persists across these actions without requiring re-authentication, and you've disabled localStorage for session storage, it's likely that cookies are being used effectively.
- **Close and Reopen Browser**: To further test the persistence, close your browser entirely and then reopen it and navigate back to your application. If you remain logged in, this indicates that the session is being stored in a way that persists beyond a single session, which is characteristic of cookie-based session management.


Server Actions being marked as stable. This means we can finally start promoting this fantastically simple way of authenticating users—entirely server-side!

export default async function Page() {
  const signIn = async () => {
    'use server'
    supabase.auth.signInWithOAuth({...})
  }

  return (
    <form action={signIn}>
      <button>Sign in with GitHub</button>
    </form>
  )
}

With Server Components, fetching data in Next.js became as simple as:

export default async function Page() {
  const { data } = await supabase.from('...').select()
  return ...
}

With Server Actions, you can now place mutation logic alongside the Server Components responsible for fetching data and rendering the page:

export default async function Page() {
  const { data } = await supabase.from('...').select()

  const createNote = async () => {
    'use server'
    await supabase.from('...').insert({...})
  }

  return ...
}

So for the App Router, that's:

Client Components
Server Components
Route Handlers
Server Actions
Middleware
VS the old Pages Router:

getServerSideProps function
getStaticProps function
API Routes
Page Components




Configuring Supabase to use Cookies
By default, supabase-js uses localStorage to store the user's session. This works well for client-side apps, but will fail when you try to use supabase-js in a Server Component, as there is no concept of 'localStorage' on the server.

To do this, we need to configure supabase-js to use cookies instead of localStorage when running on the server. But this code is a little verbose to ask people to duplicate across every app they build with Supabase:

const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    flowType: 'pkce',
    autoRefreshToken: false,
    detectSessionInUrl: false,
    persistSession: true,
    storage: {
      getItem: async (key: string) => {
        cookieStore.get(key)
      },
      setItem: async (key: string, value: string) => {
        cookieStore.set(key, value)
      },
      removeItem: async (key: string) => {
        cookieStore.remove(key)
      },
    },
  },
})

That takes care of the server-side pieces of Next.js, but since we recommend securing your apps with Row Level Security (RLS) policies, you can safely access your user's session client-side too. Therefore, we need to tell the browser how access that cookie too:

const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    flowType: 'pkce',
    autoRefreshToken: true,
    detectSessionInUrl: true,
    persistSession: true,
    storage: {
      getItem: async (key: string) => {
        return parse(document.cookie[key])
      },
      setItem: async (key: string, value: string) => {
        document.cookie = serialize(key, value)
      },
    },
    removeItem: async (key: string) => {
      document.cookie = serialize(key, '', {
        maxAge: 0,
      })
    },
  },
})

That is a lot of very confusing code! So we decided to create a package called @supabase/ssr
