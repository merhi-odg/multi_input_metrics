import logging
import pandas

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


# modelop.init
def init():
    logger.info("Now executing init function")
      
# modelop.score
def score(x):
    logger.info("Now executing score function with input %d ", x)
    yield {"input": x}

# modelop.metrics
def metrics(df1, df2, df3):
    logger.info("Now executing metrics function with inputs: \n")
    logger.info(df1)
    logger.info(df2)
    logger.info(df3)
    
    yield {
        "df1_shape": str(df1.shape),
        "df2_shape": str(df2.shape),
        "df3_shape": str(df3.shape)
    }
