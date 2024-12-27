import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "@supabase/auth-helpers-react";

// Mock function to check subscription status. Replace with your actual API call.
async function checkSubscriptionStatus(userId: string): Promise<boolean> {
  // Implement the API call to check the subscription status
  // For demonstration, this returns true to simulate a subscribed user.
  return true;
}

export const SubscriberGuard = ({ children }) => {
  const router = useRouter();
  const { session, error } = useSession();
  const [isSubscribed, setIsSubscribed] = useState<boolean | null>(null);

  useEffect(() => {
    "use client";
    if (!session) {
      // If there's no session, redirect to sign-in page
      router.push("/signin");
    } else {
      // Check if the user is subscribed
      checkSubscriptionStatus(session.user.id).then((status) => {
        if (!status) {
          // If not subscribed, redirect to a different page, e.g., subscription page
          router.push("/subscribe");
        } else {
          setIsSubscribed(true);
        }
      });
    }
  }, [session, router]);

  if (isSubscribed === null) {
    // While checking subscription status, you might want to render nothing or a loader
    return <div>Loading...</div>;
  }

  if (isSubscribed) {
    // Render children if the user is subscribed
    return <>{children}</>;
  }

  // If not subscribed, this will not be reached due to the redirect
  return null;
};

