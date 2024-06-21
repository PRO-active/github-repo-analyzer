import os
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.document_loaders import GitLoader
from langchain.indexes import VectorstoreIndexCreator

# Streamlit UI
st.title('GitHubリポジトリ解析ツール')
st.write('OpenAI APIキー、GitHubリポジトリURL、および解析するファイルの拡張子を入力してください。')

api_key = st.text_input('OpenAI APIキー', type='password')
repo_url = st.text_input('GitHubリポジトリURL')
branch = st.text_input('ブランチ名（デフォルトはmain）', 'main')
llm_models = ['gpt-3.5-turbo','gpt-4o']
llm = st.selectbox('回答出力モデル', llm_models)

file_ext_options = ['すべてのファイル', '.py', '.js', '.md', '.txt', 'その他']
file_ext_selection = st.selectbox('ファイル拡張子', file_ext_options)

if file_ext_selection == 'その他':
    file_ext = st.text_input('ファイル拡張子を指定してください（例: .rb など）')
else:
    file_ext = 'all' if file_ext_selection == 'すべてのファイル' else file_ext_selection

query = st.text_input('質問', 'Explain the code')

if st.button('回答の出力'):
    if api_key and repo_url:
        os.environ['OPENAI_API_KEY'] = api_key
        repo_path = "./temp/"

        if os.path.exists(repo_path):
            clone_url = None
        else:
            clone_url = repo_url

        try:
            if file_ext == "all":
                loader = GitLoader(
                    clone_url=clone_url,
                    branch=branch,
                    repo_path=repo_path,
                )
            else:
                loader = GitLoader(
                    clone_url=clone_url,
                    branch=branch,
                    repo_path=repo_path,
                    file_filter=lambda file_path: file_path.endswith(file_ext),
                )

            index = VectorstoreIndexCreator(
                vectorstore_cls=Chroma,
                embedding=OpenAIEmbeddings(disallowed_special=()),
            ).from_loaders([loader])
            llm = OpenAI(model=llm,temperature=0) 

            answer = index.query(query, llm=llm)

            st.write('### 回答:')
            st.write(answer)

        except Exception as e:
            st.error(f'エラー: {str(e)}')
    else:
        st.error('OpenAI APIキーとGitHubリポジトリURLの両方を入力してください。')