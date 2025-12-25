import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Dashboard des livres",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: white;
    }
    .css-1d391kg {
        background-color: white;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def init_database():
    conn = sqlite3.connect('books_database.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            price REAL NOT NULL,
            copies_sold INTEGER NOT NULL,
            rating REAL NOT NULL,
            publication_year INTEGER NOT NULL,
            publisher TEXT,
            pages INTEGER
        )
    """)
    books_data = [
('La Bibliothèque de Minuit', 'Matt Haig', 'Fiction', 15.99, 2500, 4.5, 2020, 'Canongate Books', 304),
('Atomic Habits', 'James Clear', 'Développement Personnel', 18.99, 5000, 4.8, 2018, 'Avery', 320),
('Project Hail Mary', 'Andy Weir', 'Science-Fiction', 17.99, 3200, 4.7, 2021, 'Ballantine Books', 496),
('Le Patient Silencieux', 'Alex Michaelides', 'Thriller', 14.99, 4100, 4.3, 2019, 'Celadon Books', 336),
('Educated', 'Tara Westover', 'Biographie', 16.99, 2800, 4.6, 2018, 'Random House', 334),
('Sapiens', 'Yuval Noah Harari', 'Non-Fiction', 19.99, 4500, 4.7, 2011, 'Harper', 443),
('Les Sept Maris d\'Evelyn Hugo', 'Taylor Jenkins Reid', 'Fiction', 15.99, 3800, 4.6, 2017, 'Atria Books', 388),
('Thinking, Fast and Slow', 'Daniel Kahneman', 'Psychologie', 20.99, 3500, 4.5, 2011, 'Farrar, Straus and Giroux', 499),
('Le Chant d\'Achille', 'Madeline Miller', 'Fiction Historique', 16.99, 2900, 4.8, 2011, 'Ecco', 352),
('Devenir', 'Michelle Obama', 'Biographie', 18.99, 6000, 4.9, 2018, 'Crown', 448),
('Hunger Games', 'Suzanne Collins', 'Jeunesse', 14.99, 5500, 4.4, 2008, 'Scholastic Press', 374),
('Dune', 'Frank Herbert', 'Science-Fiction', 17.99, 4200, 4.6, 1965, 'Chilton Books', 688),
('L\'Alchimiste', 'Paulo Coelho', 'Fiction', 13.99, 4800, 4.2, 1988, 'HarperOne', 208),
('Là où chantent les écrevisses', 'Delia Owens', 'Fiction', 16.99, 5200, 4.7, 2018, 'G.P. Putnam\'s Sons', 384),
('Le Pouvoir du Moment Présent', 'Eckhart Tolle', 'Développement Personnel', 17.99, 3300, 4.4, 1997, 'New World Library', 236),
('Le Code Da Vinci', 'Dan Brown', 'Thriller', 15.99, 4700, 4.1, 2003, 'Doubleday', 689),
('1984', 'George Orwell', 'Fiction', 14.99, 3900, 4.7, 1949, 'Secker & Warburg', 328),
('Gatsby le Magnifique', 'F. Scott Fitzgerald', 'Fiction', 12.99, 3400, 4.4, 1925, 'Charles Scribner\'s Sons', 180),
('Ne Tirez Pas Sur L’Oiseau Moqueur', 'Harper Lee', 'Fiction', 14.99, 4300, 4.8, 1960, 'J.B. Lippincott & Co.', 324),
('Harry Potter à l\'École des Sorciers', 'J.K. Rowling', 'Fantasy', 19.99, 7500, 4.9, 1997, 'Bloomsbury', 309),
    ]
    
    cursor.executemany("""
        INSERT INTO books (title, author, genre, price, copies_sold, rating, publication_year, publisher, pages)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, books_data)
    
    conn.commit()
    return conn

def extract_data(conn):
    query = "SELECT * FROM books"
    df = pd.read_sql_query(query, conn)
    return df

def transform_data(df):
    df['revenue'] = df['copies_sold'] * df['price']
    genre_stats = df.groupby('genre').agg({
        'id': 'count',
        'copies_sold': 'sum',
        'revenue': 'sum',
        'rating': 'mean',
        'price': 'mean'
    }).reset_index() 
    genre_stats.columns = ['genre', 'nombre_livres', 'ventes_totales', 'revenu_total', 'note_moyenne', 'prix_moyen']
    genre_stats = genre_stats.round(2)
    
    return df, genre_stats

conn = init_database()

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2702/2702154.png", width=100)
    st.title("📚 Navigation")

    menu = st.radio(
        "Choisissez une section:",
        ["🏠 Accueil", "📊 Vue d'ensemble", "📈 Analyses par Genre", 
         "🏆 Best-Sellers", "⭐ Évaluations", "🗄️ Base de Données"],
        label_visibility="collapsed"
    )
    st.divider()
    if st.button("🔄 Actualiser les données", width='stretch'):
        st.cache_data.clear()
        st.rerun()
    
    st.divider()
    st.markdown("### 📖 À propos")
    st.info("Dashboard ETL pour l'analyse des livres et leurs statistiques de vente.")

df = extract_data(conn)
df_transformed, genre_stats = transform_data(df)
total_books = len(df)
total_sales = df['copies_sold'].sum()
total_revenue = df_transformed['revenue'].sum()
avg_rating = df['rating'].mean()


st.title("Dashboard ETL des livres")
st.markdown("Analyse Complète des Données")
st.divider()

if menu == "Accueil":
    st.markdown("## Bienvenue sur le Dashboard d'Analyse des Livres")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📚 Total Livres",
            value=f"{total_books}",
            delta="Base complète"
        )
    
    with col2:
        st.metric(
            label="📦 Ventes Totales",
            value=f"{total_sales:,}",
            delta="+12% ce mois"
        )
    
    with col3:
        st.metric(
            label="💰 Revenu Total",
            value=f"${total_revenue:,.2f}",
            delta="+8.3%"
        )
    
    with col4:
        st.metric(
            label="⭐ Note Moyenne",
            value=f"{avg_rating:.2f}/5",
            delta="+0.2"
        )
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Processus ETL")
        st.success(" **Extract**: Données extraites de SQLite")
        st.info(" **Transform**: Calculs et agrégations effectués")
        st.warning(" **Load**: Visualisations chargées")
        
        st.markdown("### 🎯 Fonctionnalités")
        st.markdown("""
        - Analyse par genre
        - Classement des best-sellers
        - Évaluations et notes
        - Statistiques détaillées
        - Graphiques interactifs
        """)
    
    with col2:
        st.markdown("### Aperçu Rapide")
        top_genres = genre_stats.nlargest(3, 'revenu_total')
        
        for idx, row in top_genres.iterrows():
            with st.container():
                st.markdown(f"""
                <div style='background-color: white; padding: 15px; border-radius: 10px; margin: 10px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                    <h4 style='color: #667eea; margin: 0;'>{row['genre']}</h4>
                    <p style='color: #333; margin: 5px 0;'>💰 Revenu: ${row['revenu_total']:,.2f}</p>
                    <p style='color: #666; margin: 5px 0;'>📚 {int(row['nombre_livres'])} livres | ⭐ {row['note_moyenne']:.1f}/5</p>
                </div>
                """, unsafe_allow_html=True)

elif menu == "📊 Vue d'ensemble":
    st.markdown("## 📊 Vue d'ensemble des Données")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_pie = px.pie(
            genre_stats,
            values='nombre_livres',
            names='genre',
            title='Distribution des Livres par Genre',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, width='stretch')
    
    with col2:
        top_revenue = df_transformed.nlargest(10, 'revenue')[['title', 'revenue']]
        fig_bar = px.bar(
            top_revenue,
            x='revenue',
            y='title',
            orientation='h',
            title='Top 10 - Livres par Revenu',
            labels={'revenue': 'Revenu ($)', 'title': 'Titre'},
            color='revenue',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_bar, width='stretch')
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_genre_sales = px.bar(
            genre_stats,
            x='genre',
            y='ventes_totales',
            title='Ventes Totales par Genre',
            labels={'ventes_totales': 'Ventes', 'genre': 'Genre'},
            color='ventes_totales',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_genre_sales,width='stretch')
    
    with col2:
        year_stats = df.groupby('publication_year').size().reset_index(name='count')
        fig_timeline = px.line(
            year_stats,
            x='publication_year',
            y='count',
            title='Publications par Année',
            labels={'publication_year': 'Année', 'count': 'Nombre de livres'},
            markers=True
        )
        fig_timeline.update_traces(line_color='#667eea', line_width=3)
        st.plotly_chart(fig_timeline, width='stretch')

elif menu == "📈 Analyses par Genre":
    st.markdown("## 📈 Analyses Détaillées par Genre")

    st.dataframe(
        genre_stats.style.background_gradient(cmap='YlOrRd', subset=['revenu_total'])
                         .background_gradient(cmap='YlGn', subset=['note_moyenne'])
                         .format({
                             'revenu_total': '${:,.2f}',
                             'ventes_totales': '{:,.0f}',
                             'note_moyenne': '{:.2f}',
                             'prix_moyen': '${:.2f}'
                         }),
        width='stretch'
    )
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_revenue = px.bar(
            genre_stats,
            x='genre',
            y='revenu_total',
            title='💰 Revenu Total par Genre',
            color='revenu_total',
            color_continuous_scale='Greens',
            labels={'revenu_total': 'Revenu ($)', 'genre': 'Genre'}
        )
        st.plotly_chart(fig_revenue, width='stretch')
    
    with col2:
        # Notes moyennes par genre
        fig_ratings = px.bar(
            genre_stats.sort_values('note_moyenne', ascending=False),
            x='genre',
            y='note_moyenne',
            title='⭐ Note Moyenne par Genre',
            color='note_moyenne',
            color_continuous_scale='RdYlGn',
            labels={'note_moyenne': 'Note Moyenne', 'genre': 'Genre'}
        )
        fig_ratings.update_yaxes(title="Y", range=[0, 5])
        st.plotly_chart(fig_ratings, width='stretch')
    
    st.divider()
    selected_genre = st.selectbox("Sélectionnez un genre pour une analyse détaillée:", genre_stats['genre'].tolist())
    
    genre_books = df_transformed[df_transformed['genre'] == selected_genre]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(" Nombre de livres", len(genre_books))
    
    with col2:
        st.metric(" Revenu total", f"${genre_books['revenue'].sum():,.2f}")
    
    with col3:
        st.metric(" Note moyenne", f"{genre_books['rating'].mean():.2f}/5")
    
    st.dataframe(
        genre_books[['title', 'author', 'price', 'copies_sold', 'rating', 'revenue']]
        .sort_values('revenue', ascending=False)
        .style.format({
            'price': '${:.2f}',
            'copies_sold': '{:,}',
            'rating': '{:.1f}',
            'revenue': '${:,.2f}'
        }),
        width='stretch')

elif menu == " Best-Sellers":
    st.markdown("##  Classement des Best-Sellers")
    
    top_n = st.slider("Afficher le Top:", 5, 20, 10)
    
    top_sellers = df_transformed.nlargest(top_n, 'copies_sold')
    
    for idx, (_, book) in enumerate(top_sellers.iterrows(), 1):
        with st.container():
            col1, col2, col3, col4 = st.columns([1, 4, 2, 2])
            
            with col1:
                st.markdown(f"### #{idx}")
            
            with col2:
                st.markdown(f"**{book['title']}**")
                st.caption(f"Par {book['author']} • {book['genre']}")
            
            with col3:
                st.metric(" Ventes", f"{book['copies_sold']:,}")
            
            with col4:
                st.metric("Revenu", f"${book['revenue']:,.2f}")
            
            st.progress(book['copies_sold'] / top_sellers['copies_sold'].max())
        
        st.divider()
    fig_comparison = go.Figure()
    
    fig_comparison.add_trace(go.Bar(
        name='Ventes',
        x=top_sellers['title'],
        y=top_sellers['copies_sold'],
        yaxis='y',
        marker_color='lightblue'
    ))
    
    fig_comparison.add_trace(go.Scatter(
        name='Revenu',
        x=top_sellers['title'],
        y=top_sellers['revenue'],
        yaxis='y2',
        marker_color='red',
        mode='lines+markers'
    ))
    
    fig_comparison.update_layout(
        title=f'Top {top_n} - Comparaison Ventes vs Revenu',
        xaxis=dict(title='Livre', tickangle=-45),
        yaxis=dict(title='Ventes', side='left'),
        yaxis2=dict(title='Revenu ($)', side='right', overlaying='y'),
        legend=dict(x=0.01, y=0.99),
        height=500
    )
    
    st.plotly_chart(fig_comparison, width='stretch')

elif menu == " Évaluations":
    st.markdown("## Analyse des Évaluations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        top_rated = df_transformed.nlargest(10, 'rating')
        
        st.markdown("### 🌟 Top 10 - Meilleures Notes")
        
        for idx, (_, book) in enumerate(top_rated.iterrows(), 1):
            with st.container():
                col_a, col_b = st.columns([3, 1])
                
                with col_a:
                    st.markdown(f"**{idx}. {book['title']}**")
                    st.caption(f"{book['author']} • {book['genre']}")
                
                with col_b:
                    stars = "⭐" * int(book['rating'])
                    st.markdown(f"{stars} **{book['rating']:.1f}**")
                
                st.divider()
    
    with col2:
        fig_dist = px.histogram(
            df,
            x='rating',
            nbins=20,
            title='Distribution des Notes',
            labels={'rating': 'Note', 'count': 'Nombre de livres'},
            color_discrete_sequence=['#667eea']
        )
        st.plotly_chart(fig_dist, width='stretch')
        fig_box = px.box(
            df,
            x='genre',
            y='rating',
            title='Distribution des Notes par Genre',
            labels={'rating': 'Note', 'genre': 'Genre'},
            color='genre'
        )
        st.plotly_chart(fig_box, width='stretch')
    
    st.divider()
    st.markdown("### 📊 Corrélation: Note vs Prix vs Ventes")
    
    fig_scatter = px.scatter(
        df_transformed,
        x='price',
        y='rating',
        size='copies_sold',
        color='genre',
        hover_data=['title', 'author'],
        title='Relation entre Prix, Note et Ventes',
        labels={'price': 'Prix ($)', 'rating': 'Note', 'copies_sold': 'Ventes'}
    )
    st.plotly_chart(fig_scatter, width='stretch')
    

elif menu == "🗄️ Base de Données":
    st.markdown("## 🗄️ Base de Données Complète")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        genre_filter = st.multiselect(
            "Filtrer par genre:",
            options=df['genre'].unique(),
            default=df['genre'].unique()
        )
    
    with col2:
        min_rating = st.slider("Note minimale:", 0.0, 5.0, 0.0, 0.1)
    
    with col3:
        min_sales = st.number_input("Ventes minimales:", 0, int(df['copies_sold'].max()), 0)

    filtered_df = df_transformed[
        (df_transformed['genre'].isin(genre_filter)) &
        (df_transformed['rating'] >= min_rating) &
        (df_transformed['copies_sold'] >= min_sales)
    ]
    
    st.markdown(f"**{len(filtered_df)} livres trouvés**")

    st.dataframe(
        filtered_df[['title', 'author', 'genre', 'price', 'copies_sold', 'rating', 'revenue', 'publication_year']]
        .sort_values('revenue', ascending=False)
        .style.format({
            'price': '${:.2f}',
            'copies_sold': '{:,}',
            'rating': '{:.1f}',
            'revenue': '${:,.2f}'
        })
        .background_gradient(cmap='YlOrRd', subset=['revenue'])
        .background_gradient(cmap='YlGn', subset=['rating']),
        width='stretch',
        height=600
    )
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Télécharger les données (CSV)",
        data=csv,
        file_name=f'books_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
        mime='text/csv',
    )
    
    st.divider()
    
    st.markdown("###  Exécuter une requête SQL personnalisée")
    
    sql_query = st.text_area(
        "Entrez votre requête SQL:",
        value="SELECT * FROM books WHERE rating > 4.5 ORDER BY copies_sold DESC LIMIT 5",
        height=100
    )
    
    if st.button(" Exécuter la requête"):
        try:
            result = pd.read_sql_query(sql_query, conn)
            st.success(f"Requête exécutée avec succès! {len(result)} résultats trouvés.")
            st.dataframe(result, width='stretch')
        except Exception as e:
            st.error(f"❌ Erreur: {str(e)}")

st.divider()
st.markdown("""
<div style='text-align: center; color: white; padding: 20px;'>
    <p>ETL Dashboard • Créé avec Streamlit & SQLite</p>
    <p>Extract • Transform • Load • Visualize</p>
</div>
""", unsafe_allow_html=True)