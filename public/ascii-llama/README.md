## NeuroScene - AI-Powered 3D Scene Creation

# Overview
Welcome to NeuroScene, a revolutionary AI-powered 3D scene creation tool that's changing the game for creators and developers. As part of the Meta Cerebral Valley Hackathon, our team is pushing the boundaries of what's possible with AI-driven design.

![GNjTh2zaYAABiaQ](https://github.com/ebowwa/ascii-llama/assets/81942069/7d555ae0-6d7c-4318-86e2-e776ed9a7bb4)

Our goal is to create an intuitive and efficient UI that enables users to create complex 3D scenes with ease. The NeuroScene AI engine will:

Read user minds: Understand user intent and create 3D scenes accordingly
Provide real-time feedback: Offer suggestions and insights to the user
Learn from user corrections: Adapt to their preferences and improve over time

## Technical Details
We're leveraging the following training data to fuel our AI finetuning:
ASCII Rendering: Text-based representations of 3D scenes
Vision-Model-Desc: Descriptions of 3D models and their properties as depicted via local `llava` model
Model Metadata: Additional metadata about the 3D models, such as their specified placements, renderings, etc.

To keep a unified source and a cleanly design we utilize two wedev frameworks
- nextjs server = http://localhost:3000 // our distribution channel
- fastapi = http://localhost:7070 `#` our training server

## Training Targets:

[ ]ASCII Scene Description: Just like Blender's scene hierarchy, the LLM could be trained to generate text that describes the structure and contents of a 3D ASCII scene. This could include the placement of ASCII characters, their sizes, orientations, and relationships to one another.

[ ]ASCII Modeling Tools: The LLM could be trained to generate text-based commands or scripts that can be used to "model" 3D ASCII shapes and objects. This could involve learning the syntax and semantics of a custom ASCII modeling language, similar to Blender's scripting capabilities.

[ ]ASCII Animation and Rigging: The LLM could be trained to generate text that describes the animation and rigging of 3D ASCII characters or objects. This could include specifying keyframes, bone structures, and other animation-related concepts in a textual format.

[ ]ASCII Lighting and Materials: The LLM could be trained to generate text that sets the lighting, shading, and material properties of a 3D ASCII scene. This could involve learning how to translate high-level lighting and material concepts into the ASCII representation.

[ ]ASCII Rendering and Compositing: The LLM could be trained to generate text that describes the rendering and compositing of a 3D ASCII scene, similar to how Blender allows users to configure render settings and compositing nodes.

[ ]ASCII Project Management: The LLM could be trained to generate text that organizes and manages the creation of 3D ASCII content, such as project files, asset libraries, and version control systems.

[ ]ASCII Visualization and Debugging: The LLM could be trained to generate text that helps visualize and debug 3D ASCII content, such as generating ASCII-based wireframes, normals, or other diagnostic information.


initial training run | poor quality & limited finetuning data, the three asset model metadata was not integrated into training and input was not validated | strisunshine/Llama-3-cerebral-valley https://huggingface.co/strisunshine/Llama-3-cerebral-valley

## Platform Frontend
