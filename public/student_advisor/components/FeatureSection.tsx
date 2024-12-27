// components/FeatureSection.tsx

interface FeatureSectionProps {
  title: string;
  description?: string;
  features?: Array<{ title: string; description: string }>;
}

export const FeatureSection: React.FC<FeatureSectionProps> = ({ title, description, features }) => {
  return (
    <section className="container py-12 md:py-24 lg:py-32">
      <div className="grid max-w-3xl gap-4 mx-auto items-start space-y-4 lg:gap-10 lg:flex lg:items-center lg:space-y-0">
        <div className="space-y-2 text-center lg:text-left">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">{title}</h2>
          {description && <p className="text-gray-500 dark:text-gray-400">{description}</p>}
        </div>
        {features && (
          <div className="space-y-4">
            {features.map((feature, index) => (
              <div key={index}>
                <h3 className="font-bold">{feature.title}</h3>
                <p>{feature.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
};
