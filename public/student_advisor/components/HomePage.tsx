// HomePage.tsx

import { HeaderSection } from "@/components/HeaderSection";
import { FeatureSection } from "@/components/FeatureSection";
import { FooterSection } from "@/components/FooterSection";

export function HomePage() {
  return (
    <>
      <HeaderSection
        title="Assist.org API"
        description="Provides data and functionality for the assist.org website."
      />
      <FeatureSection
        title="Endpoints"
        description="Available API endpoints with a brief description of their purpose."
        features={[
          { title: "/courses", description: "Retrieve course data." },
          { title: "/majors", description: "Retrieve major data." },
          { title: "/institutions", description: "Retrieve institution data." },
        ]}
      />
      <FeatureSection
        title="Authentication"
        description="The Assist.org API requires an API key for authentication. To obtain an API key, please contact our support team."
      />
      <FooterSection />
    </>
  );
}
