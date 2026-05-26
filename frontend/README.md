# Campus Currency Frontend

Frontend application for the **Campus Currency** platform built using **Flutter**.

This project follows a **feature-first modular architecture** to keep the codebase scalable, maintainable, and team-friendly as the platform grows.

---

# Current Tech Stack

| Layer            | Technology                      |
| ---------------- | ------------------------------- |
| Framework        | Flutter                         |
| State Management | Riverpod                        |
| Routing          | go_router                       |
| Networking       | Dio                             |
| Local Storage    | Hive                            |
| Secure Storage   | flutter_secure_storage          |
| Architecture     | Feature-first modular structure |

---

# Current Project Structure

```text
lib/
│
├── core/
├── features/
├── routes/
├── shared/
│
├── app.dart
└── main.dart
```

---

# Folder Explanations

---

# lib/core/

Contains global app infrastructure and reusable foundational code.

This layer should NOT contain feature-specific business logic.

```text
core/
├── constants/
├── network/
├── services/
├── storage/
├── theme/
├── utils/
└── widgets/
```

---

## core/constants/

Stores global constants used across the application.

Examples:

* API URLs
* app-wide configuration values
* route names
* static strings

Example files:

```text
api_constants.dart
app_constants.dart
```

---

## core/network/

Handles networking setup and API infrastructure.

Responsibilities:

* Dio client setup
* interceptors
* token handling
* request/response configuration

Example files:

```text
dio_client.dart
api_interceptor.dart
```

---

## core/services/

Contains reusable global services.

Examples:

* authentication service
* notification service
* analytics service

These services are typically shared across multiple features.

---

## core/storage/

Handles local storage infrastructure.

Examples:

* Hive setup
* secure token storage
* caching utilities

---

## core/theme/

Contains the global app theme and design system.

Responsibilities:

* colors
* typography
* spacing
* dark/light themes
* reusable styling

Current file:

```text
app_theme.dart
```

---

## core/utils/

General utility/helper functions.

Examples:

* date formatting
* validators
* helper methods
* extensions

---

## core/widgets/

Reusable widgets shared across the entire app.

Examples:

* custom buttons
* loading indicators
* reusable cards
* custom dialogs

Goal:
Avoid duplicating UI code across features.

---

# lib/features/

Contains all feature modules.

Each feature should remain mostly self-contained.

Current structure:

```text
features/
├── auth/
├── dashboard/
└── wallet/
```

Future features can be added later:

```text
clubs/
events/
reputation/
admin/
```

---

# Feature Structure Philosophy

Each feature should ideally contain:

```text
feature_name/
│
├── data/
├── domain/
└── presentation/
```

This keeps:

* UI
* business logic
* data handling

cleanly separated.

---

# dashboard/

Currently contains the dashboard UI layer.

```text
dashboard/
└── presentation/
    └── screens/
```

---

## presentation/

Contains UI-related code.

Includes:

* screens
* widgets
* providers/state management

---

## screens/

Contains full application pages/screens.

Current file:

```text
dashboard_screen.dart
```

---

# auth/

Will contain:

* login
* registration
* authentication flow
* token/session management

Planned structure:

```text
auth/
├── data/
├── domain/
└── presentation/
```

---

# wallet/

Will contain:

* wallet UI
* balance display
* transaction history
* transfers
* ledger visualization

---

# lib/routes/

Contains centralized navigation configuration.

Responsibilities:

* app routes
* navigation guards
* route definitions

Planned:

```text
app_router.dart
```

---

# lib/shared/

Contains shared resources used across multiple features.

Examples:

* common models
* shared enums
* reusable providers

Used when code does not belong to a single feature.

---

# Root Files

---

# main.dart

Application entry point.

Responsibilities:

* initialize Flutter
* initialize Riverpod
* start the app

---

# app.dart

Main application configuration.

Responsibilities:

* theme setup
* root navigation
* top-level app configuration

---

# Current Architecture Goals

This structure is designed to:

* scale cleanly as features grow
* support multiple contributors
* reduce code duplication
* separate UI from business logic
* keep features modular
* simplify long-term maintenance

---

# Development Principles

## 1. Reusable UI First

Avoid repeating components.

If a widget appears in multiple places:
move it into:

```text
core/widgets/
```

---

## 2. Keep Business Logic Out of Screens

Screens should primarily handle:

* layout
* rendering
* user interaction

NOT:

* API logic
* storage logic
* complex processing

---

## 3. Feature Isolation

Each feature should own:

* its screens
* its providers
* its repositories
* its models

Avoid unnecessary cross-feature dependencies.

---

## 4. Modular Growth

The project currently only includes:

* auth
* dashboard
* wallet

Additional modules should only be added when needed.

Avoid premature complexity.

---

# Current Status

✅ Flutter project initialized
✅ Git connected
✅ Base architecture created
✅ Dark theme configured
✅ Dashboard screen setup
✅ Riverpod installed
✅ Clean project structure established

---

# Immediate Next Steps

1. Setup routing (`go_router`)
2. Create reusable UI components
3. Build dashboard layout
4. Implement authentication flow
5. Build wallet interface
6. Connect backend APIs later

---

# Recommended Git Workflow

create a feature branch for every new function
