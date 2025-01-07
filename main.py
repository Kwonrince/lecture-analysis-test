from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, CommaSeparatedListOutputParser, StrOutputParser
import boto3
import os
import re
import json
from datetime import datetime
from pydantic import BaseModel
import importlib
import shutil
from utils import utils
import pandas as pd
from utils.time_converter import TimeConverter
importlib.reload(utils)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")