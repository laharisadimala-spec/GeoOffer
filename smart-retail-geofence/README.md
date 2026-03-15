# AI-Driven Geofencing Based Intelligent Offer Recommendation System

## Module: Geofencing & Location Detection

This module detects when a user enters a store location using GPS and triggers an event to generate personalized offers.

---

## How It Works

1. The application requests the user's location using the browser Geolocation API.
2. The system continuously tracks the user's latitude and longitude.
3. A virtual boundary (geofence) is created around the store location.
4. The distance between the user and the store is calculated.
5. If the user enters the geofence radius, the system triggers an event.
6. This event sends a request to the backend API to generate a personalized offer.

---

## Technologies Used

- JavaScript
- Browser Geolocation API
- Leaflet Maps
- HTML & CSS
- REST API integration

---

## Key Features

- Real-time GPS location tracking
- Geofence detection around store locations
- Map visualization with store and user markers
- Automatic offer trigger when entering store area
- Backend API communication for AI recommendations

---

## System Flow

User Location  
↓  
Geofence Detection  
↓  
Store Entry Event  
↓  
Backend API Call  
↓  
AI Generates Personalized Offer  

---

## Demo Functionality

- Displays store location on the map
- Tracks the user’s live GPS location
- Shows a geofence circle around the store
- Triggers an offer when the user enters the geofence

---

## Purpose

This module enables retailers to send personalized promotions to customers at the exact moment they enter a store location, improving engagement and sales.