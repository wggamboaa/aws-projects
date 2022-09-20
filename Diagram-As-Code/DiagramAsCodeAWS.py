
# Importamos el módulo maestro Diagram
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.aws.analytics import GlueDataCatalog
from diagrams.aws.analytics import Glue
from diagrams.aws.analytics import Athena
from diagrams.aws.analytics import Redshift
from diagrams.aws.analytics import Quicksight
from diagrams.aws.analytics import LakeFormation
from diagrams.aws.ml import SagemakerNotebook
from diagrams.aws.ml import Sagemaker
from diagrams.aws.ml import SagemakerModel
from diagrams.aws.ml import SagemakerTrainingJob
from diagrams.generic.device import Mobile
from diagrams.generic.device import Tablet
from diagrams.generic.database import SQL
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.database import DatabaseMigrationService
from diagrams.aws.database import Redshift
from diagrams.saas.alerting import Opsgenie
from diagrams.saas.analytics import Snowflake
from diagrams.aws.devtools import Codecommit
from diagrams.aws.devtools import Codebuild
from diagrams.aws.devtools import Codedeploy
from diagrams.aws.devtools import Codepipeline
from diagrams.aws.security import IdentityAndAccessManagementIam
from diagrams.aws.management import Cloudwatch
from diagrams.aws.cost import CostManagement
from diagrams.aws.security import Shield
from diagrams.saas.social import Facebook
from diagrams.saas.social import Twitter
from diagrams.aws.database import Dynamodb
from diagrams.aws.analytics import EMR
from diagrams.aws.integration import StepFunctions
from diagrams.saas.filesharing import Nextcloud
from diagrams.aws.compute import Lambda
from diagrams.onprem.database import Oracle
from diagrams.onprem.database import Mongodb

with Diagram(name="Data Mesh Architecture AppJedi on AWS", show=False) as diag:
  with Cluster("Dominio Data Lake"):
    with Cluster("Data Source"):
      with Cluster("Near / Real Time"):
            mb_dl=Mobile("API Aplication")
            tb_dl=Tablet("App Mobile")
      with Cluster("Batch"):
            sql_dl=SQL("OLTP")
    with Cluster("Data Ingestion"):
      with Cluster("Streaming"):
            kn_di=KinesisDataFirehose("Kinesis Data Firehose")
      with Cluster("Batch"):
            dms_di=DatabaseMigrationService("Database Migration Service")
    with Cluster("Data Storage Layer"):
      dc_un_dl=GlueDataCatalog("Glue Data Catalog")
      with Cluster("Landing Zone"):
         with Cluster("Low Cost Zone"):
            sss1Bronze_un_dl=SimpleStorageServiceS3Bucket("S3")
      with Cluster("Proccesing Zone"):
          with Cluster("ETL / ELT"):
            glueStep1_un_dl=Glue("Glue")
            sfunc_un_dl=Glue("StepFunctions")
      with Cluster("Curated Data Zone"):
          with Cluster("Datawarehouse"):
            redshift_un_dl=Redshift("Redshift")
          with Cluster("DataLake"):
            sss1Gold_un_dl=SimpleStorageServiceS3Bucket("S3")
    with Cluster("Consumption Zone"):
      with Cluster("Analytics"):
         with Cluster("Dashboards"):
            qs_un_dl=Quicksight("Quicksight")
      with Cluster("Data Science"):
          with Cluster("Workspace"):
            sg_un_dl=Sagemaker("Sagemaker")
      with Cluster("Custom Aplications"):
          with Cluster("Adhoc"):
            ops_un_dl=Opsgenie("Aplication")
    with Cluster("Data Ops"):
            cd_do_dl = Codedeploy("Codedeploy")
            cp_do_dl = Codepipeline("Codepipeline")
            cu_do_dl = Codebuild("Codebuild")
            cc_do_dl = Codecommit("Codecommit")
    with Cluster("Security, Data Catalog, Governance"):
            lf_ctg_un_dl = LakeFormation("LakeFormation")
            iam_cdg_un_dl = IdentityAndAccessManagementIam("IAM")
    with Cluster("Observability, Maintenance, Operation"):
            cw_omp_un_dl = LakeFormation("Cloudwatch")
            lf_omp_un_dl = LakeFormation("CostManagement")
            sh_omp_un_dl = LakeFormation("Shield")
  #Dominio Data Lake      
  [mb_dl,tb_dl] >> kn_di
  sql_dl >> dms_di
  [kn_di,dms_di] >> sss1Bronze_un_dl >> glueStep1_un_dl
  glueStep1_un_dl >> [redshift_un_dl,sss1Gold_un_dl]
  redshift_un_dl >> [qs_un_dl,ops_un_dl]
  sss1Gold_un_dl >> sg_un_dl
  cc_do_dl >> [cd_do_dl,cu_do_dl,cp_do_dl]
  dc_un_dl >> lf_ctg_un_dl
  cc_do_dl >> [lf_ctg_un_dl, iam_cdg_un_dl]
  
  with Cluster("Dominio Social Lake"):
    with Cluster("Data Source"):
      with Cluster("Near / Real Time"):
            mb_sl=Mobile("API Aplication")
            fb_sl=Facebook("Facebook")
            tw_sl=Twitter("Twitter")
    with Cluster("Data Ingestion"):
      with Cluster("Streaming"):
            kn_sl=KinesisDataFirehose("Kinesis Data Firehose")
    with Cluster("Data Storage Layer"):
      dc_un_sl=GlueDataCatalog("Glue Data Catalog")
      with Cluster("Landing Zone"):
        with Cluster("Low Cost Zone"):
            dynamo_un_sl=Dynamodb("Dynamodb")
      with Cluster("Proccesing Zone"):
          with Cluster("ETL / ELT"):
            emr_un_sl=EMR("EMR")
            sfunc_un_sl=Glue("StepFunctions")
      with Cluster("Curated Data Zone"):
          with Cluster("Datawarehouse"):
            redshift_un_sl=Redshift("Redshift")
          with Cluster("DataLake"):
            sss1Gold_un_sl=SimpleStorageServiceS3Bucket("S3")
    with Cluster("Consumption Zone"):
      with Cluster("Analytics"):
         with Cluster("Dashboards"):
            qs_un_sl=Quicksight("Quicksight")
      with Cluster("Data Science"):
          with Cluster("Workspace"):
            sg_un_sl=Sagemaker("Sagemaker")
      with Cluster("Custom Aplications"):
          with Cluster("Adhoc"):
            ops_un_sl=Opsgenie("Aplication")
    with Cluster("Data Ops"):
            cd_do_sl = Codedeploy("Codedeploy")
            cp_do_sl = Codepipeline("Codepipeline")
            cu_do_sl = Codebuild("Codebuild")
            cc_do_sl = Codecommit("Codecommit")
    with Cluster("Security, Data Catalog, Governance"):
            lf_ctg_un_sl = LakeFormation("LakeFormation")
            iam_cdg_un_sl = IdentityAndAccessManagementIam("IAM")
    with Cluster("Observability, Maintenance, Operation"):
            cw_omp_un_sl = LakeFormation("Cloudwatch")
            lf_omp_un_sl = LakeFormation("CostManagement")
            sh_omp_un_sl = LakeFormation("Shield")
  #Dominio Social Lake
  [fb_sl,tw_sl] >> mb_sl >> kn_sl
  kn_sl >> dynamo_un_sl >> emr_un_sl
  emr_un_sl >> [redshift_un_sl,sss1Gold_un_sl]
  redshift_un_sl >> [qs_un_sl,ops_un_sl]
  sss1Gold_un_sl >> sg_un_sl
  cc_do_sl >> [cd_do_sl,cu_do_sl,cp_do_sl]
  dc_un_sl >> lf_ctg_un_sl
  cc_do_sl >> [lf_ctg_un_sl, iam_cdg_un_sl]

  with Cluster("Dominio Machine Learning Lake"):
    with Cluster("Data Source"):
      with Cluster("Unstructured / Semi-structured"):
            nl_ml=Nextcloud("Nextcloud")
    with Cluster("Data Ingestion"):
      with Cluster("Batch"):
            ld_ml=Lambda("Lambda")
    with Cluster("Data Storage Layer"):
      dc_un_ml=GlueDataCatalog("Glue Data Catalog")
      with Cluster("Landing Zone"):
         with Cluster("Low Cost Zone"):
            sss1Bronze_un_ml=SimpleStorageServiceS3Bucket("S3")
      with Cluster("Proccesing Zone"):
          with Cluster("ETL / ELT"):
            emr_un_ml=EMR("EMR")
            sfunc_un_ml=Glue("StepFunctions")
      with Cluster("Curated Data Zone"):
          with Cluster("Datawarehouse"):
            redshift_un_ml=Redshift("Redshift")
          with Cluster("DataLake"):
            sss1Gold_un_ml=SimpleStorageServiceS3Bucket("S3")
    with Cluster("Consumption Zone"):
      with Cluster("Analytics"):
         with Cluster("Dashboards"):
            qs_un_ml=Quicksight("Quicksight")
      with Cluster("Data Science"):
          with Cluster("Workspace"):
            sg_un_ml=Sagemaker("Sagemaker")
            dc_unsg_ml=GlueDataCatalog("ML Data Catalog")
            sss1_un_ml=SimpleStorageServiceS3Bucket("Working Data")
            sgn_un_ml=SagemakerNotebook("Sagemaker Notebook")
            sgm_un_ml=SagemakerNotebook("Sagemaker Model")
            sgtj_un_ml=SagemakerNotebook("Sagemaker Training Job")
      with Cluster("Custom Aplications"):
          with Cluster("Data Sharing"):
           sss1Sharing_un_ml=SimpleStorageServiceS3Bucket("S3")
    with Cluster("Data Ops"):
            cd_do_ml = Codedeploy("Codedeploy")
            cp_do_ml = Codepipeline("Codepipeline")
            cu_do_ml = Codebuild("Codebuild")
            cc_do_ml = Codecommit("Codecommit")
    with Cluster("Security, Data Catalog, Governance"):
            lf_ctg_un_ml = LakeFormation("LakeFormation")
            iam_cdg_un_ml = IdentityAndAccessManagementIam("IAM")
    with Cluster("Observability, Maintenance, Operation"):
            cw_omp_un_ml = LakeFormation("Cloudwatch")
            lf_omp_un_ml = LakeFormation("CostManagement")
            sh_omp_un_ml = LakeFormation("Shield")
  #Dominio Machine Learning Lake      
  nl_ml >> ld_ml
  ld_ml >> sss1Bronze_un_ml >> emr_un_ml
  emr_un_ml >> [redshift_un_ml,sss1Gold_un_ml]
  redshift_un_ml >> [qs_un_ml,sss1Sharing_un_ml]
  sss1Gold_un_ml >> sg_un_ml
  cc_do_ml >> [cd_do_ml,cu_do_ml,cp_do_ml]
  dc_un_ml >> lf_ctg_un_ml
  cc_do_ml >> [lf_ctg_un_ml, iam_cdg_un_ml]
  [sgm_un_ml,sgtj_un_ml] >> sss1_un_ml
  sg_un_ml >> sss1_un_ml
  [sg_un_ml,sgn_un_ml] >> dc_unsg_ml

  with Cluster("Dominio Analytics Lake"):
    with Cluster("Data Source"):
      with Cluster("Batch"):
            oracle_al=Oracle("Oracle")
            mongo_al=Mongodb("Mongodb")
    with Cluster("Data Ingestion"):
      with Cluster("Batch"):
            dms_al=DatabaseMigrationService("Database Migration Service")
    with Cluster("Data Storage Layer"):
      dc_un_al=GlueDataCatalog("Glue Data Catalog")
      with Cluster("Landing Zone"):
         with Cluster("Low Cost Zone"):
            sss1Bronze_un_al=SimpleStorageServiceS3Bucket("S3")
      with Cluster("Proccesing Zone"):
          with Cluster("ETL / ELT"):
            glueStep1_un_al=Glue("Glue")
            sfunc_un_al=Glue("StepFunctions")
      with Cluster("Curated Data Zone"):
          with Cluster("Datawarehouse"):
            redshift_un_al=Redshift("Redshift")
          with Cluster("DataLake"):
            sss1Gold_un_al=SimpleStorageServiceS3Bucket("S3")
    with Cluster("Consumption Zone"):
      with Cluster("Analytics"):
         with Cluster("Dashboards"):
            qs_un_al=Quicksight("Quicksight")
            athena_un_al=Athena("Athena")
            sss1working_un_al=SimpleStorageServiceS3Bucket("Working Data")
      with Cluster("Data Science"):
          with Cluster("Workspace"):
            sg_un_al=Sagemaker("Sagemaker")
      with Cluster("Custom Aplications"):
          with Cluster("Data Sharing"):
           sss1Sharing_un_al=SimpleStorageServiceS3Bucket("S3")
    with Cluster("Data Ops"):
            cd_do_al = Codedeploy("Codedeploy")
            cp_do_al = Codepipeline("Codepipeline")
            cu_do_al = Codebuild("Codebuild")
            cc_do_al = Codecommit("Codecommit")
    with Cluster("Security, Data Catalog, Governance"):
            lf_ctg_un_al = LakeFormation("LakeFormation")
            iam_cdg_un_al = IdentityAndAccessManagementIam("IAM")
    with Cluster("Observability, Maintenance, Operation"):
            cw_omp_un_al = LakeFormation("Cloudwatch")
            lf_omp_un_al = LakeFormation("CostManagement")
            sh_omp_un_al = LakeFormation("Shield")
  #Dominio Analytics Lake      
  [oracle_al,mongo_al] >> dms_al
  dms_al >> sss1Bronze_un_al >> glueStep1_un_al
  glueStep1_un_al >> [redshift_un_al,sss1Gold_un_al]
  redshift_un_al >> [qs_un_al,sss1Sharing_un_al]
  sss1Gold_un_al >> [sg_un_al,sss1working_un_al]
  [athena_un_al,qs_un_al] >> sss1working_un_al
  cc_do_al >> [cd_do_al,cu_do_al,cp_do_al]
  dc_un_al >> lf_ctg_un_al
  cc_do_al >> [lf_ctg_un_al, iam_cdg_un_al]

diag    