Based on the provided non-functional requirements for the "Campus Exploration Event" project, the following functional requirements document has been created:

# Functional Requirements Document

## 1. Introduction
This functional requirements document defines the necessary functionalities for the "Campus Exploration Event" application, aiming to ensure a successful and engaging event experience. The application will guide participants through various campus locations, facilitating interactions through photo uploads and analysis.

## 2. User Registration and Authentication

### 2.1 User Registration
- Function to allow new users to register for the event using their email and creating a password.
- Users should be able to register using OAuth (Google, Facebook).

### 2.2 User Login
- Function to allow registered users to log in using their email and password.
- Option for users to log in using OAuth (Google, Facebook).
- Implement multi-factor authentication (MFA) as an added security measure.

### 2.3 Password Recovery
- Function to allow users to recover their password using their email.

## 3. Event Participation

### 3.1 Event Home Screen
- Display event details such as event name, schedule, and instructions.
- Show a list of tasks or challenges that participants need to complete.

### 3.2 Task List
- Present tasks or challenges that participants can select.
- Each task will have a description, location, and the ability to start/completed status.

### 3.3 Task Details
- Show detailed instructions for each task including the location and any required actions such as taking a photo.

## 4. Photo Upload and Analysis

### 4.1 Photo Capture
- Function allowing users to take photos using the app's built-in camera feature or uploading from their device's gallery.

### 4.2 Photo Upload
- Facilitate the upload of captured photos to the server.
- Limit the size of the photos to ensure quick uploads.

### 4.3 Photo Analysis
- Server-side functionality to analyze uploaded photos, verify task completion, and provide instant feedback.
- Analysis results should be displayed within 5 seconds.

## 5. User Interaction and Engagement

### 5.1 Real-Time Feedback
- Provide real-time feedback on the completed tasks and points scored.
- Inform users about the successful or unsuccessful completion of tasks.

### 5.2 Leaderboard
- Feature a real-time leaderboard to display top participants based on points scored.
- Allow users to view their rank and the ranks of other participants.

### 5.3 Notifications
- Send notifications to users about upcoming tasks, events, or important updates.
- Notifications can be in-app or through push notifications.

## 6. Social Media Integration

### 6.1 Share on Social Media
- Allow users to share their achievements and photos on social media platforms such as Facebook, Twitter, and Instagram.

## 7. User Feedback

### 7.1 Feedback Form
- Provide a feedback form where users can submit their experiences, issues, or suggestions.

### 7.2 Feedback Collection
- The feedback collected should be stored in a database for analysis and subsequent improvements.

## 8. Administration and Management

### 8.1 Admin Dashboard
- Dashboard for event administrators to monitor the event's progress, manage tasks, and view user participation data.
- Allow administrators to add, edit, or delete tasks.

### 8.2 User Management
- Functionality for administrators to view and manage user accounts.
- Allow administrators to ban or delete accounts if necessary.

### 8.3 Event Metrics
- Provide detailed metrics and analytics about user participation, task completion rates, and overall event engagement.

## 9. Multi-Language Support

### 9.1 Language Selection
- Allow users to select the app's language (Japanese or English).
- Automatically detect and set the language based on the user’s device settings.

## 10. Compatibility

### 10.1 Mobile Platforms
- The app should be fully functional on both iOS and Android platforms.

### 10.2 Web Compatibility
- Provide a web version of the app that works seamlessly on Chrome, Safari, Firefox, and Edge.

## 11. Legal and Compliance

### 11.1 Privacy Policy
- Include a privacy policy that complies with relevant laws such as GDPR.
- Ensure users are aware of how their data is collected, used, and protected.

## 12. Risk Management

### 12.1 Data Backup
- Implement real-time data backup to prevent data loss.
- Ensure backup data is stored securely and can be quickly restored in case of system failure.

### 12.2 Disaster Recovery
- Define a disaster recovery plan to handle unexpected system failures.
- Ensure system recovery within 15 minutes of a failure.

## 13. Training and Support

### 13.1 User Training
- Provide detailed tutorials and help sections within the app.
- Ensure users understand how to use the app effectively.

### 13.2 Support Channels
- Provide multiple support channels such as email, chat, and phone to assist users during the event.
- Ensure a swift response to user queries and issues.

Above functional requirements, when integrated with the provided non-functional requirements, will help build a robust, secure, and user-friendly application for the "Campus Exploration Event", enhancing user engagement and ensuring a successful event.