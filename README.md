## Project Descriptions

### 📈 Stock Market Predictor (Python + ML)

A hands-on exploration of time-series data and simple machine-learning baselines for price movement prediction. The project emphasizes an end-to-end workflow—collecting historical data, engineering interpretable features, fitting baseline models, evaluating properly, and visualizing results—rather than “beating the market.”

- **Purpose:** Practice real data workflows and ML hygiene (train/test splits, leakage avoidance, basic metrics) on financial time series.
- **What it does:** Downloads OHLCV data, builds features (returns, rolling means/volatility, lags), trains baseline models, and plots predictions vs. actuals.
- **Tech Stack:** `Python`, `pandas`, `yfinance`, `NumPy`, `scikit-learn`, `matplotlib`/`Jupyter`.
- **Key Features:** Reproducible data loading, quick feature pipelines, baseline regressors/classifiers, error metrics (MAE/MSE/accuracy), and side-by-side charts.
- **Skills Practiced:** Data wrangling, feature engineering, ML evaluation, plotting, notebook organization.
- **Possible Extensions:** Walk-forward cross-validation, more robust feature sets, model comparison (tree-based, linear, simple LSTM), and experiment tracking.

---

### 🛒 Amazon-Style E-Commerce Clone (React + Firebase + Stripe)

A full-stack practice app that recreates core e-commerce flows—product browsing, cart, authentication, and a mock checkout—using modern frontend patterns and managed cloud services.

- **Purpose:** Learn how to structure a React application, manage global state, and connect a frontend to real backends (auth, database, payments).
- **What it does:** Renders a product catalog, supports add-to-cart and quantity updates, authenticates users, persists data in Firestore, and runs a test checkout via Stripe/Firebase Functions.
- **Tech Stack:** `React`, `React Router`, Context/Reducer (or similar state), `Firebase` (Auth, Firestore, Hosting, Functions), `Stripe` (test mode), `Node.js` tooling.
- **Key Features:** Protected routes, persistent cart, order history, responsive UI, serverless functions for payment intents/verification, and easy deploy with Firebase Hosting.
- **Skills Practiced:** SPA routing, state management, auth flows, schema design in NoSQL, serverless APIs, environment configuration.
- **Possible Extensions:** Admin dashboard (CRUD for products), real Stripe webhooks, inventory management, search/filters, accessibility and unit tests.

---

### 👤 Face Recognition + Attendance (OpenCV)

A computer-vision demo that recognizes known faces in real time and logs attendance. It covers image preprocessing, face embeddings, real-time inference, and simple logging/UX with on-screen overlays.

- **Purpose:** Get practical experience with classical CV pipelines and face embeddings for recognition/verification tasks.
- **What it does:** Encodes reference images, detects faces from webcam frames, matches embeddings to known identities, overlays names/confidence, and logs timestamps to a CSV/text file.
- **Tech Stack:** `Python`, `OpenCV`, `face_recognition` (dlib under the hood), `NumPy`.
- **Key Features:** One-time face encoding, real-time detection/matching, lightweight UI overlays, and append-only attendance logs for later analysis.
- **Skills Practiced:** Image I/O, real-time processing loops, embeddings and distance thresholds, simple data logging, basic troubleshooting of native deps (e.g., dlib).
- **Possible Extensions:** Database backend (SQLite/Postgres), GUI (Tkinter/PyQt), multi-camera support, batching/queuing, and exporting analytics dashboards.
