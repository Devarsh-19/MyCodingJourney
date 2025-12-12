──────────────────────────────────────────────────────────────
                    PRESENTATION LAYER
──────────────────────────────────────────────────────────────
Frontend (React / Streamlit)
   - Uploads CSV → API
   - Displays spend analytics
   - Chat interface for financial advice

──────────────────────────────────────────────────────────────
                    API & SERVICE LAYER (FastAPI)
──────────────────────────────────────────────────────────────
1. Ingestion Service
   - CSV/Excel parsing
   - Standardization
   - Transaction creation
   - Category prediction via MLflow model

2. RAG Financial Advisor Service
   - SQL summarization engine
   - Hybrid retriever:
       • User transaction embeddings
       • Finance knowledge embeddings
   - Prompt builder
   - LLM inference
   - Advice logging

3. User Feedback Service
   - Stores advice ratings
   - Feeds into retraining pipelines

──────────────────────────────────────────────────────────────
                    DATA & STORAGE LAYER
──────────────────────────────────────────────────────────────
1. Relational Database (Postgres/MySQL)
   Tables:
   - users
   - transactions
   - source_files
   - advice_logs
   - feedback

2. Vector Database (Qdrant/Pinecone/Weaviate)
   Collections:
   - user_transaction_embeddings
   - finance_knowledge_embeddings

3. Object Storage / File Store
   - Original user statements
   - Pre-processed text chunks
   - Knowledge documents

──────────────────────────────────────────────────────────────
                    MACHINE LEARNING LAYER
──────────────────────────────────────────────────────────────
1. MLflow Model Registry
   - Stores transaction category classifier
   - Stores LLM adapters (Fine-tuned models)

2. Classification Model Pipeline
   - Feature engineering
   - Model training
   - Evaluation, logging, registration

3. RAG Index Builder
   - Embedding generation
   - Batch indexing of transactions
   - Maintenance of vector DB

4. Advisory LLM Engine
   - Chat model
   - RAG orchestrator (LangChain/LlamaIndex)

──────────────────────────────────────────────────────────────
                    MLOps / AUTOMATION LAYER
──────────────────────────────────────────────────────────────
1. Orchestration (Airflow / Prefect)
   • Daily ingestion job
   • Weekly model retraining
   • Weekly RAG indexing job
   • LLM fine-tuning pipeline

2. Monitoring Layer
   - Model drift detection
   - Feedback analytics
   - Query/response logging
   - System health dashboards

3. CI/CD (GitHub Actions)
   - Test → Build → Deploy
   - Auto-deploy updated ML models
   - Auto-redeploy backend services

──────────────────────────────────────────────────────────────
                    DEPLOYMENT LAYER
──────────────────────────────────────────────────────────────
Dockerized Services
   - api-service
   - worker-service (pipelines)
   - vector-db-service (optional local)
   - mlflow-service

Deployment Targets
   - AWS ECS / Fargate
   - GCP Cloud Run
   - Azure App Service
   - Railway / Render
