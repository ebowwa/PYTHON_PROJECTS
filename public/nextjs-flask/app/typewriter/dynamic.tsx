import React from 'react';
import { useTypewriterEffect } from '../typewriter/typewriter';
import styles from '../typewriter/TypewriterEffect.module.css'; // Adjust the import path as necessary

interface DynamicTextComponentProps {
  name: string;
  interestMessage: string;
  roles: string[];
}

const DynamicTextComponent: React.FC<DynamicTextComponentProps> = ({ name, interestMessage, roles }) => {
  const dynamicText = useTypewriterEffect(roles);

  return (
    <div className={`${styles.typewriter} profile-header`}>
      <h1>{name}</h1>
      <p>{interestMessage}</p>
      <h2>I'm a {dynamicText}</h2>
      {/* Social media icons would go here */}
    </div>
  );
};

export default DynamicTextComponent;
