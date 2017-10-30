class AcquisitorAndCleaner(EngineBaseDataHandler):
    
    def execute(self, **kwargs):
        data = self.spark.sql("""select p.bscprd_desc as name,
        h.misphr_line as tag from core.mis_product_hierarchy as h,
        core.bsc_product as p 
        where h.misphr_id_product = p.bscprd_id_product 
        and h.misphr_line in ('SMARTPHONE', 'TABLETS')""")
        self.initial_dataset = data.toPandas()