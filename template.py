import os 
from pathlib import Path

prj_name = "us_visa"  

files_list = [

    f"{prj_name}/__init__.py",
    f"{prj_name}/components/__init.py__",
    f"{prj_name}/components/data_ingestion.py",
    f"{prj_name}/components/data_validation.py",
    f"{prj_name}/components/data_transformation.py",
    f"{prj_name}/components/model_trainer.py",
    f"{prj_name}/components/model_evaluation.py",
    f"{prj_name}/components/model_pusher.py",
    f"{prj_name}/configurations/__init.py__",
    f"{prj_name}/constants/__init__.py",
    f"{prj_name}/entity/__init__.py",
    f"{prj_name}/entity/config_entity.py",
    f"{prj_name}/entity/artifact_entity.py",
    f"{prj_name}/exception/__init__.py",
    f"{prj_name}/logger/__init__.py",
    f"{prj_name}/pipline/__init__.py",
    f"{prj_name}/pipline/training_pipeline.py",
    f"{prj_name}/pipline/prediction_pipeline.py",
    f"{prj_name}/utils/__init__.py",
    f"{prj_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

for file in files_list:
    file_path = Path(file)
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents= True, exist_ok= True)
    if not file_path.exists() or file_path.stat().st_size == 0:
        file_path.write_text("")
    else:
        print(f"File already exists: {file_path}")
    
