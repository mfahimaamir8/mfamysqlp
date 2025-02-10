import streamlit as st
st.write("Muhammad is the Bes ")
import pandas as pd
from streamlit_js_eval import streamlit_js_eval
import mysql.connector

#Host: sql12.freesqldatabase.com
#Database name: sql12745454
#Database user: sql12745454
#Database password: y8pwdlLWN5
#Port number: 3306


#host = 9r-1o.h.filess.io
#dbname  = mfaerpdb_behaviorme
#user = mfaerpdb_behaviorme
#port = 3307
#pwd   = 6d9a14c6f222ec9f3c724a611c8a184e5d01ed9f

#db naame = mfaerpdb_behaviorme

#connectin formate

#mydb = mysql.connector.connect(
#conn = mysql.connector.connect(
#  host="9r-1o.h.filess.io",
#  user="mfaerpdb_behaviorme",
 # password="6d9a14c6f222ec9f3c724a611c8a184e5d01ed9f",
 # database="mfaerpdb_behaviorme",
 # port=3307
#)


conn = mysql.connector.connect(
  host="hq3-6.h.filess.io",
  user="mfadb_strongwill",
  password="ffad1e1cd30388902ba276d26c3b4f6042dacd45",
  database="mfadb_strongwill",
  port=3307
)



#mydb = mysql.connector.connect(  host="sql12.freesqldatabase.com",  user="sql12745454",  password="y8pwdlLWN5",  database="sql12745454",  port=3306)



#print(mydb)
#print("muhammad is the best")

curr = conn.cursor()
curr.execute("select * from stable")
data = curr.fetchall()
#print(curr.column_names)
st.title('Muhammad is the Best all over the universes')
df = pd.DataFrame(data,columns=curr.column_names)
mdf = st.data_editor(df,num_rows="dynamic",key="demo_df")
#st.write(mdf)
edited_rows = st.session_state["demo_df"]
st.write(edited_rows)




co1, co2,co3 = st.columns(3)

with co1:
  ttt = st.session_state["demo_df"].get("added_rows")
  st.write(ttt)
  ttt2 = pd.DataFrame(ttt) 
  st.write(ttt2)
  rows = [tuple(x) for x in ttt2.values]
  st.write(rows)
  #st.dataframe(df)
  if st.button('Save New Data'):
        st.write("muhammad is the best ")
        rows = [tuple(x) for x in ttt2.values]
        insert_query = "INSERT INTO stable (sname , sfee , fdate ,recsta) VALUES (%s, %s, %s, %s)"
        for row in rows:
          curr.execute(insert_query, row)
        conn.commit()
        conn.close()
        streamlit_js_eval(js_expressions="parent.window.location.reload()")


with co2:
  ttt = st.session_state["demo_df"].get("edited_rows")
  st.write(ttt)
  ttt2 = pd.DataFrame(ttt) 
  st.write(ttt2)
  rows = [tuple(x) for x in ttt2.values]
  st.write(rows)
  #st.dataframe(df)
  if st.button('Save Edit Data'):
        st.write("muhammad is the best ")
        rows = [tuple(x) for x in ttt2.values]
        insert_query = "INSERT INTO stable (sname , sfee , fdate ,recsta) VALUES (%s, %s, %s, %s)"
        for row in rows:
          curr.execute(insert_query, row)
        conn.commit()
        conn.close()
        streamlit_js_eval(js_expressions="parent.window.location.reload()")




with co3:
  delrow = st.session_state["demo_df"].get("deleted_rows")
  #rowsind = st.session_state.df.loc[delrow] 
  st.write(delrow)
  delete_rows = df.loc[delrow] 
  delspcol = delete_rows[['recsta','sno']]
  delspcol = delspcol.assign(recsta='mfadel')
  st.write(delspcol)
  if st.button('ST.editdata'):
    sql = 'UPDATE stable SET recsta = %s WHERE sno = %s '
    for index, row in delspcol.iterrows():
      curr.execute(sql, [row['recsta'], row['sno']])
      #curr.commit()
      conn.commit()
      #conn.close()
      streamlit_js_eval(js_expressions="parent.window.location.reload()")
  
  
  
  
  #SQL query to INSERT a record into the table FACTRESTTBL.
    #cursor.execute('''INSERT into FACTRESTTBL (id, city)     values (%s, %s)''',        (id, city))

    # Commit your changes in the database
    #db.commit()

# disconnect from server
#db.close()


    
#if st.button('ST.editdata'):
#    st.write("muhammad is the best --------------")
 #   streamlit_js_eval(js_expressions="parent.window.location.reload()")
  #  #curr.close()
    





#sql = 'UPDATE tblhis_ventas SET portabilidad = ? WHERE contrato = ? and estado = ?'
#for index, row in df.iterrows():
#cursor.execute(sql, [row['portabilidad'], row['contrato'], row['estado']])

# Prepare an INSERT query with placeholders for each column
# Assuming Payments table has 4 columns as an example



# Insert each row into the table

# Commit the transaction


# Close the connection

#"sname":"ffgh"
#"fee":345
#"feedata":"202

#"edited_rows":{}
#"added_rows":[]
#"deleted_rows":[]
