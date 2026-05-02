-- 1. HABILITAR A EXTENSÃO pgvector
-- Habilita as funcionalidades de armazenamento e busca de vetores no PostgreSQL.
-- A cláusula "if not exists" garante que o comando não falhe se a extensão já estiver ativa.
create extension if not exists vector;

-- 2. CRIAR A TABELA 'documents'
-- Esta tabela armazenará os chunks de texto, seus metadados e os vetores de embedding correspondentes.
create table
  documents (
    id bigserial primary key,
    content text not null, -- Armazena o texto original do chunk.
    metadata jsonb, -- Campo flexível para metadados (ex: nome do arquivo, nº da página).
    embedding vector(768) -- Vetor de embedding. A dimensão 768 corresponde ao modelo do Google (embedding-001).
  );

-- 3. CRIAR A FUNÇÃO RPC 'match_documents'
-- Esta função será chamada pela aplicação (via LangChain) para encontrar os chunks mais relevantes
-- para uma determinada pergunta.
create or replace function match_documents (
  query_embedding vector(768),
  match_count int default null,
  filter jsonb default '{}'
) returns table (
  id bigint,
  content text,
  metadata jsonb,
  similarity float
) language plpgsql as $$
#variable_conflict use_column
begin
  return query
  select
    id,
    content,
    metadata,
    1 - (documents.embedding <=> query_embedding) as similarity -- Calcula a similaridade de cosseno.
  from
    documents
  where
    metadata @> filter -- Permite a filtragem opcional por metadados.
  order by
    documents.embedding <=> query_embedding -- Ordena pela distância (menor é melhor).
  limit
    match_count;
end;
$$;

-- 4. CRIAR O ÍNDICE PARA OTIMIZAÇÃO DA BUSCA
-- Cria um índice HNSW nos vetores para acelerar drasticamente as buscas por similaridade.
-- A busca por similaridade de cosseno (vector_cosine_ops) é a mais comum em aplicações RAG.
-- O número de listas (lists) pode ser ajustado conforme o volume de dados, mas 100 é um bom ponto de partida.
create index on documents using hnsw (embedding vector_cosine_ops);

-- Para referência, um índice IVFFlat seria criado da seguinte forma:
-- create index on documents using ivfflat (embedding vector_cosine_ops) with (lists = 100);
-- No entanto, HNSW é geralmente recomendado para um melhor balanço entre performance e precisão.
