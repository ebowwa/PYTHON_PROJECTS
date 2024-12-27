import { useState, useEffect, useRef } from 'react';

// Custom hook to implement the typewriter effect
export const useTypewriterEffect = (roles: string[], typingSpeed = 200, deletingSpeed = 100, pauseBeforeDeleting = 2000, pauseBeforeTypingNext = 500) => {
  const [dynamicText, setDynamicText] = useState('');
  const roleIndexRef = useRef(0);
  const typingTimeoutRef = useRef<number | null>(null);

  useEffect(() => {
    const typeWriterEffect = () => {
      const currentRole = roles[roleIndexRef.current];
      let charIndex = 0;

      const typeChar = () => {
        if (charIndex < currentRole.length) {
          setDynamicText(currentRole.slice(0, charIndex + 1));
          charIndex++;
          typingTimeoutRef.current = window.setTimeout(typeChar, typingSpeed);
        } else {
          typingTimeoutRef.current = window.setTimeout(deleteChar, pauseBeforeDeleting);
        }
      };

      const deleteChar = () => {
        if (charIndex > 0) {
          setDynamicText(currentRole.slice(0, charIndex - 1));
          charIndex--;
          typingTimeoutRef.current = window.setTimeout(deleteChar, deletingSpeed);
        } else {
          roleIndexRef.current = (roleIndexRef.current + 1) % roles.length;
          typingTimeoutRef.current = window.setTimeout(typeChar, pauseBeforeTypingNext);
        }
      };

      typeChar();
    };

    typeWriterEffect();

    return () => {
      if (typingTimeoutRef.current !== null) {
        clearTimeout(typingTimeoutRef.current);
      }
    };
  }, [roles, typingSpeed, deletingSpeed, pauseBeforeDeleting, pauseBeforeTypingNext]);

  return dynamicText;
};
// curl -X POST -F "file=@api/_backend/public/wrestling.mp4" http://127.0.0.1:5328/api/upload
