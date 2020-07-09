FROM rackspacedot/python37
RUN pip install streamlit 
WORKDIR /src
ADD src /src
ENTRYPOINT ["streamlit","run"]
CMD ["covidnepal.py"]
