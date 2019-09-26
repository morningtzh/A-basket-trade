import jqdatasdk

jqdatasdk.auth("18605712083", "sbbuzhidaomima")

a = jqdatasdk.finance.run_query(query(finance.STK_SHAREHOLDER_TOP10).filter(finance.STK_SHAREHOLDER_TOP10.code==code).limit(n))
